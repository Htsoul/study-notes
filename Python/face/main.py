import cv2 as cv

img = cv.imread('huge.png')
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_img',gray_img)
cv.imwrite('gray_huge.png',gray_img)

cv.imshow('_img',img)

cv.waitKey(0)

cv.destroyAllWindows()