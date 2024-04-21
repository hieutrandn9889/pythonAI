import cv2
import imutils

# read image and gray image color
image = cv2.imread("sample.png")

# open the image
cv2.imshow("Anh mau", image)
cv2.waitKey()


# convert blurred image
# ksize always parity
blurImage = cv2.GaussianBlur(image, ksize=(31,31), sigmaX=0)
cv2.imshow("Anh blur", blurImage)
cv2.waitKey()

# press any to quit
cv2.destroyAllWindows()