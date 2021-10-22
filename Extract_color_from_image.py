import cv2
import numpy as np

## 使用する画像指定 jpgでもpngでも可
img = cv2.imread("./a.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## hsvで抜き出す色の範囲を指定
# mask = cv2.inRange(hsv, (36, 0, 0), (86, 255,255))  #green
# mask = cv2.inRange(hsv, (5, 0, 0), (30, 255,255))  # red
mask = cv2.inRange(hsv, (100, 0, 0), (120, 255,255)) #blue

imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## 保存するファイル名　jpgでもpngでも可
cv2.imwrite("image.png", green)