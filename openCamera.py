import cv2

#number camera 
# open your camera
# camera_id = 0 

camera_id = "sample.avi"

# open camera
cap = cv2.VideoCapture(camera_id)

# read image from camera 
# using while is loop when user press "q" to quit
while True:
    # read any frame
    ret, frame = cap.read()
    # show iamge
    cv2.imshow("Cam", frame)
    # press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# quit camera
cap.release()
cv2.destroyAllWindows()