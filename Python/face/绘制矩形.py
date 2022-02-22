import cv2 as cv

img = cv.imread('huge.png')
x,y,w,h = 100,100,100,100
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)
cv.circle(img,center=(x+w,y+h),radius=100, color=(255,0,0),thickness=5)
cv.imshow('re_img',img)
cv.imshow('_img',img)

cv.waitKey(0)

cv.destroyAllWindows()