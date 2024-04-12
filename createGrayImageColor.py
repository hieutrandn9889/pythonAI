import cv2

# read image and gray image color
image = cv2.imread("same.png", cv2.IMREAD_GRAYSCALE)

# create gray image color
cv2.imwrite("sameGray.png", image)