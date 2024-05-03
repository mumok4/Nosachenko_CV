import cv2
from skimage.measure import euler_number

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
image = cv2.imread("Nosachenko.png")

video = cv2.VideoCapture("pictures.avi")
n = 0
while (video.isOpened()):
    ret, frame = video.read()
    if not ret:
        break
    cv2.putText(frame, f"Number of my images = {n}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))

    thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(thresh, 50, 255, cv2.THRESH_BINARY_INV)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow("Image", frame)

    if cnts:
        figure = cnts[0]

        (x, y), radius = cv2.minEnclosingCircle(figure)
        center = (int(x), int(y))
        radius = int(radius)

        outer_circle = cv2.circle(frame, center, radius, (0, 255, 0), 2)
        circle_area = radius ** 2 * 3.14

        if (cv2.contourArea(figure)/circle_area) >= 0.16 and (cv2.contourArea(figure)/circle_area) <= 0.162 and euler_number(figure) == 1:
            n += 1

        if cv2.waitKey(50) == ord("q"):
            break

print(f"Final number of my images = {n}")

video.release()
cv2.destroyAllWindows()