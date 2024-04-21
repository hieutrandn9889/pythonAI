import cv2

# read image and gray image color
image = cv2.imread("sample.png")

# open the image
cv2.imshow("Anh mau", image)
cv2.waitKey()

# resize double image
imageResize = cv2.resize(image, dsize=None, fx=2, fy=2)
cv2.imshow("Anh Resize", imageResize)
cv2.waitKey()

# press any to quit
cv2.destroyAllWindows()