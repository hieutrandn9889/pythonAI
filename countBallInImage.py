import cv2
import imutils

# read image and gray image color
image = cv2.imread("sample.png")

# open the image
cv2.imshow("Anh mau", image)
cv2.waitKey()

# convert to gray image
grayImage = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)


edeges = cv2.Canny(grayImage, threshold1=100, threshold2=200)
cv2.imshow("Anh edge", edeges)
cv2.waitKey()

# press any to quit
cv2.destroyAllWindows()