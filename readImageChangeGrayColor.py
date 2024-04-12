import cv2

# read image and gray image color
image = cv2.imread("same.png", cv2.IMREAD_GRAYSCALE)

# show image with title: "Anh"
cv2.imshow("Anh", image)

# stop screen
cv2.waitKey()

# close window
cv2.destroyWindow()