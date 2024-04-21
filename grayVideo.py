import cv2

cameraID = "sample.avi"

video = cv2.VideoCapture(cameraID)
rotate = 0

while True:
    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Anh tu webcam", frame)
    if cv2.waitKey(1) == ord('c'):
        break

video.release()
cv2.destroyAllWindows()