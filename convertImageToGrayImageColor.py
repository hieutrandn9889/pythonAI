import cv2

# read image and gray image color
image = cv2.imread("sample.png")

# open the image
cv2.imshow("Anh mau", image)
cv2.waitKey()

# convert image to gray color
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Anh xam", imageGray)
cv2.waitKey()

# press any to quit
cv2.destroyAllWindows()