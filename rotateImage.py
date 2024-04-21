import cv2
import imutils

# read image and gray image color
image = cv2.imread("sample.png")

# open the image
cv2.imshow("Anh mau", image)
cv2.waitKey()

# rotate double image
# 45o
imageRotate = imutils.rotate(image, 45)
cv2.imshow("Anh Rotate 45", imageRotate)
cv2.waitKey()

# press any to quit
cv2.destroyAllWindows()