import cv2
import zmq
import numpy as np

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("Mask", cv2.WINDOW_GUI_NORMAL)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
port = 5055
socket.connect(f"tcp://192.168.0.113:{port}")

while True:
    bts = socket.recv()
    arr = np.frombuffer(bts, np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    _, thresh = cv2.threshold(hsv[:, :, 1], 70, 255, cv2.THRESH_BINARY)
    distance_map = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    ret, dist_thresh = cv2.threshold(distance_map, 0.4 * np.max(distance_map), 255, cv2.THRESH_BINARY)

    confuse = cv2.subtract(thresh, dist_thresh.astype("uint8"))

    ret, marker = cv2.connectedComponents(dist_thresh.astype("uint8"))
    marker += 1
    marker[confuse == 255] = 0

    segments = cv2.watershed(image, marker)
    cnts, hierarchy = cv2.findContours(dist_thresh.astype(np.uint8), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    ball_count = 0
    cube_count = 0

    for i in range(len(cnts)):
        if hierarchy[0][i][3] == -1:
            area = cv2.contourArea(cnts[i])
            if area < 100:  # Ignore small contours that are likely noise
                continue

            perimeter = cv2.arcLength(cnts[i], True)
            if perimeter == 0:
                continue
            circularity = 4 * np.pi * (area / (perimeter * perimeter))

            if circularity > 0.7:  # Heuristic: shapes with circularity close to 1 are balls
                ball_count += 1
                cv2.drawContours(image, [cnts[i]], -1, (255, 0, 0), 2)
            else:
                cube_count += 1
                cv2.drawContours(image, [cnts[i]], -1, (0, 255, 0), 2)

    cv2.putText(image, f"Balls: {ball_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (127, 255, 255))
    cv2.putText(image, f"Cubes: {cube_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (127, 255, 255))

    cv2.imshow("Image", image)
    cv2.imshow("Mask", confuse)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
