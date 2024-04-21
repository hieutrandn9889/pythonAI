import cv2
import imutils

# read image and gray image color
image = cv2.imread("sample.png")

# open the image
cv2.imshow("Anh mau", image)
cv2.waitKey()

# convert to gray image
grayImage = cv2.cvtColor(image,cv2.COLOR_BAYER_BG2GRAY)

# apply threshold
# if < 127 then 0
# if > 127 then 255
ret, threshBinary = cv2.threshold(grayImage, 127,255,cv2.THRESH_BINARY)
cv2.imshow("Anh threshold", grayImage)
cv2.waitKey()

# press any to quit
cv2.destroyAllWindows()