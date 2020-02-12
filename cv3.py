import cv2
import numpy as np 
img = cv2.imread('vlcsnap-error810.png')

px = img[100,100]
print(px)

blue = img[100,100,0]
print(blue)

img[100,100] = [255,255,255]
img[100,50] = [230,150,65]
print(img[100,100])
print(img[100,50])

print(img.size)
print(img.dtype)
print("...........................")


ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()



