import cv2

# read image and gray image color
image = cv2.imread("sample.png", cv2.IMREAD_GRAYSCALE)

# create gray image color
cv2.imwrite("sampleGray.png", image)