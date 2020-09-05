# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:55:33 2020

@author: Bilustack
"""


import cv2
import numpy as np


img = cv2.imread("components/flower.png")
G_img = cv2.imread("components/flower.png",0)

r, c = G_img.shape
win = 255 * np.ones((r,c,3),np.uint8)
#cv2.imshow("window",win)
#cv2.waitKey(0)

pen = cv2.imread("components/pen2.png")
r_pen = cv2.resize(pen,(40,40))

for i in range(0,r):
    j=0
    for k in range(i,0-1,-1):
        if i%2 == 0:
            if G_img[ k , j] < 255:
                
                "Animation part"
                win[ k+1:k+1+40, j+1:j+1+40] = r_pen
                win[k , j ] = img [k , j]
                
                cv2.imshow("window",win)
                win[ k+1:k+1+40, j+1:j+1+40] = 255
        else:
            if G_img[ j , k] < 255:
                
                "Animation part"
                win[ j+1:j+1+40, k+1:k+1+40] = r_pen
                win[j,k] = img [ j,k ]
                
                cv2.imshow("window",win)
                win[ j+1:j+1+40, k+1:k+1+40] = 255
        j=j+1

    des = cv2.waitKey(10)
    if des == 27:
        break


for i in range(1,r):
    j=i
    for k in range(c-1,i-1,-1):
        if i%2 == 0:
            if G_img[ k , j] < 255:
                
                "Animation part"
                win[ k+1:k+1+40, j+1:j+1+40] = r_pen
                win[k , j ] =img[k,j]
                
                cv2.imshow("window",win)
                win[ k+1:k+1+40, j+1:j+1+40] = 255
        else:
            if G_img[ j , k] < 255:
                
                "Animation part"
                win[ j+1:j+1+40, k+1:k+1+40] = r_pen
                win[j , k ] = img[j,k]
                
                cv2.imshow("window",win)
                win[j+1:j+1+40, k+1:k+1+40] = 255
        j=j+1

    des = cv2.waitKey(10)
    if des == 27:
        break
      

cv2.imshow("window",win)
cv2.waitKey(0)
cv2.destroyAllWindows()