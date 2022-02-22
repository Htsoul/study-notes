import cv2 as cv

img = cv.imread('huge.png')
size_img = cv.resize(img,dsize=(200,200))
cv.imshow('gray_img',size_img)

cv.imshow('_img',img)
print('修改前：', img.shape)
print('修改后：', size_img.shape)
cv.waitKey(0)

cv.destroyAllWindows()