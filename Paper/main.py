import cv2
import zmq
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
port = 5055
socket.connect(f"tcp://192.168.0.113:{port}")

bts = socket.recv()
arr = np.frombuffer(bts, np.uint8)
image = cv2.imdecode(arr, cv2.IMREAD_COLOR)

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("Mask", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("T", cv2.WINDOW_GUI_NORMAL)

lower = 100
upper = 200


def lower_update(value):
    global lower
    lower = value


def upper_update(value):
    global upper
    upper = value


cv2.createTrackbar("Lower", "Mask", lower, 255, lower_update)
cv2.createTrackbar("Upper", "Mask", upper, 255, upper_update)

while 1:
    bts = socket.recv()
    arr = np.frombuffer(bts, np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    mask = cv2.Canny(gray, lower, upper)
    cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts) == 0:
        continue

    cnt = max(cnts, key=cv2.contourArea)

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.intp(box)

    width, height = int(rect[1][0]), int(rect[1][1])
    if width < height:
        width, height = height, width

    pts1 = np.float32(box)
    pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(image, M, (width, height))

    cv2.putText(warped, "Sample Text", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)

    M_inv = cv2.getPerspectiveTransform(pts2, pts1)
    transformed_back = cv2.warpPerspective(warped, M_inv, (image.shape[1], image.shape[0]))

    mask_transformed_back = cv2.cvtColor(transformed_back, cv2.COLOR_BGR2GRAY)
    ret, mask_transformed_back = cv2.threshold(mask_transformed_back, 1, 255, cv2.THRESH_BINARY)

    image_bg = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask_transformed_back))

    combined = cv2.add(image_bg, transformed_back)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break

    cv2.imshow("Image", combined)
    cv2.imshow("Mask", mask)
    cv2.imshow("T", image)

cv2.destroyAllWindows()
