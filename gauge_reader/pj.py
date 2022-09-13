from skimage.exposure import is_low_contrast
import imutils
import numpy as np
import time
from math import sqrt ,pi
import cv2
import collections

import math
from fastnumbers import fast_real
from skimage.transform import (hough_line, hough_line_peaks)
from imutils import perspective
from collections import Counter
from PIL import Image
import pandas as pd
from functions import gauge_edges,detect_zero,convert_img_to_BGR,region_of_interest,find_min_max_angel,dist_2_pts,get_contour_areas,midpoint,most_frequent,draw_text,adjust_gamma
from IPython.display import clear_output, Image
def zoom(image, zoom_factor=2):
    return cv2.resize(image, None, fx=zoom_factor, fy=zoom_factor)



v_path="D:\phthon\opencv_pj\WIN_20220405_11_28_55_Pro.mp4"
print("Accessing Video Stream")
vs = cv2.VideoCapture(v_path)
if vs :
    print("Accessing Video Stream")

angels=[]
needle_angel=[]
printed = False
min_angle= 0.0
max_angle = 0.0
needle_angel_=0.0
while True :
  (grabbed , frame ) = vs.read()
  # if the frame not grabbing means that we reach the end
  if not grabbed :
    print("No frame read from the steam")
    break
  # resize the frame , convert it to grayscale , bluer it and then do edge detection
  frame =  imutils.resize(frame,width= 450)
  # # new line
  frame= adjust_gamma(frame,gamma=1.4)
  cv2.imwrite("gamma_frame.jpg",frame)
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray,(5,5),0)
  edged = cv2.Canny(blurred,30,30)
  text = "Low contrast : No"
  color = (0,255,0)

  # for low contrast
  if is_low_contrast(gray,fraction_threshold=0.15):
    text = "Low contrast : Yes "
    color= (0,0,255)
  else :

    # find contours in edged img and find the largest one
    cnts = cv2.findContours(edged.copy() , cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
    cnts= imutils.grab_contours(cnts)
    c= max(cnts,key= cv2.contourArea)
    peri=cv2.arcLength(c,True)
    approx= cv2.approxPolyDP(c,0.04*peri,True)
    if len(approx)==8:
        k=cv2.isContourConvex(approx)
        print(k)
        area=cv2.contourArea(c)
        r = sqrt(area/pi)
        #print(r)

        # compute the center of the contour
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        mask = np.zeros(frame.shape, dtype=np.uint8)

        # draw the rectangle around the contour and the center of the shape on the image
        cv2.rectangle(frame, (cX-(int(r)+15), cY-(int(r)+15)), (cX+(int(r)+15),cY+(int(r)+15)), (0,255,0), 1)
        cv2.circle(frame, (cX, cY), 5, (0,255,0), -1)
        cv2.circle(frame, (cX, cY), int(r), (0, 255, 0), thickness=2)
        # draw the circle adges
        gauge_edges(cX,cY,int(r),frame)
        cv2.circle(mask, (cX,cY), int(r)-10, (255,255,255), -1)

        # Bitwise-and for ROI
        ROI = cv2.bitwise_and(frame, mask)

        # Crop mask and turn background white
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        x,y,w,h = cv2.boundingRect(mask)
        result = ROI[y:y+h,x:x+w]
        mask = mask[y:y+h,x:x+w]
        result[mask==0] = (255,255,255)
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        k=convert_img_to_BGR(result)
        canny= cv2.Canny(gray, 120, 255)
        int_cnt= []
        thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)[1]
        cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        c_= max(cnts,key= cv2.contourArea)
        M = cv2.moments(c_)
        cX_ = int(M["m10"] / M["m00"])
        cY_ = int(M["m01"] / M["m00"])
        #cv2.circle(frame[y:y+h,x:x+w], (cX_,cY_), 2, (255,255,255), -1)
        text_2 = "Not Detected"
        color_2=(0,0,255)
        center_points = []
        for cnt in cnts:
            area = cv2.contourArea(cnt)
            x_,y_,w_,h_=cv2. boundingRect(cnt)
            if area > 1000:
                M = cv2.moments(cnt)
                cX_ = int(M["m10"] / M["m00"])
                cY_ = int(M["m01"] / M["m00"])

                center_points.append([cX_,cY_])
                cv2.drawContours(frame[y:y+h,x:x+w], cnt, -1, (0,255,0), 2)
                cv2.circle(frame[y:y+h,x:x+w], (cX_,cY_), 4, (255, 0, 0), 2)
            elif area >200 and area <800:
                    extremeLeft = tuple(cnt[cnt[:, :, 0].argmin()][0])
                    cv2.drawContours(frame[y:y+h,x:x+w], [cnt], -1, (0,255,0), 2)
                    cv2.circle(frame[y:y+h,x:x+w], extremeLeft, 3, (0, 0, 255), -1)
                    x_,y_=extremeLeft
                    p1 = (cX_,cY_)
                    p2 = (x_, y_)
                    theta = np.arctan2(p1[1]-p2[1], p1[0]-p2[0])
                    endpt_x = int(p1[0] - r*np.cos(theta))
                    endpt_y = int(p1[1] - r*np.sin(theta))
                    Zero_line=[]
                    cv2.line(frame[y:y+h,x:x+w], (p1[0], p1[1]), (endpt_x, endpt_y), (0, 255, 0), 1)
                    dist_pt0_needle = dist_2_pts(p1[0], p1[1],p1[0], p1[1])
                    dist_pt1_needle = dist_2_pts(p1[0], p1[1],endpt_x, endpt_y)

                    if (dist_pt0_needle > dist_pt1_needle):
                        xlen= p1[0]-p1[0]
                        ylen= p1[1]-p1[1]
                    else:
                        xlen= endpt_x-p1[0]
                        ylen= p1[1]-endpt_y

                    #Taking arc-tan of ylen/xlen to find the angle
                    res= np.arctan(np.divide(float(abs(ylen)), float(abs(xlen))))
                    res= np.rad2deg(res)

                    if xlen<0 and ylen>0:
                        angel= res+90
                        if angel :
                         needle_angel.append(angel)
                    if xlen>0 and ylen>0:
                        angel= 270-res
                        if angel :
                         needle_angel.append(angel)
                    if xlen>0 and ylen<0:
                        angel= 270+res
                        if angel :
                         needle_angel.append(angel)
                    if xlen<0 and ylen<0:
                        angel= 90-res
                        if angel :
                         needle_angel.append(angel)

            X,Y,W,H = cv2.boundingRect(cnt)
            area = W / float(H)
            #print(X,Y,W,H)
            Width = W > 2 and W <6
            Height = H > 3 and H < 15
            Area = area > 0

            if all((Width,Height,Area)):
                #print(X,Y,W,H)
                int_cnt.append(cnt)
                len_list = len(int_cnt)

                if  len_list > 0  :
                    text_2 = "Detected"
                    color_2=(0,255,0)
                #print(center_points)
                for i in range(len(center_points)):
                    p1 = (center_points[0][0],center_points[0][1] )
                    p2 = (X,Y)
                    theta = np.arctan2(p1[1]-p2[1], p1[0]-p2[0])
                    endpt_x = int(p1[0] - r*np.cos(theta))
                    endpt_y = int(p1[1] - r*np.sin(theta))

                    cv2.line(frame[y:y+h,x:x+w], (p1[0], p1[1]), (endpt_x, endpt_y), (0, 255, 0), 1)

                    dist_pt0 = dist_2_pts(p1[0], p1[1],p1[0], p1[1])
                    dist_pt1 = dist_2_pts(p1[0], p1[1],endpt_x, endpt_y)

                    if (dist_pt0 > dist_pt1):
                        xlen= p1[0]-p1[0]
                        ylen= p1[1]-p1[1]
                    else:
                        xlen= endpt_x-p1[0]
                        ylen= p1[1]-endpt_y

                    #Taking arc-tan of ylen/xlen to find the angle
                    res= np.arctan(np.divide(float(abs(ylen)), float(abs(xlen))))
                    res= np.rad2deg(res)

                    if xlen<0 and ylen>0:
                        angel= res+90
                        if angel  :
                          angels.append(angel)
                    if xlen>0 and ylen>0:
                        angel= 270-res
                        if angel  :
                          angels.append(angel)
                    if xlen>0 and ylen<0:
                        angel= 270+res
                        if angel  :
                          angels.append(angel)
                    if xlen<0 and ylen<0:
                        angel= 90-res
                        if angel  :
                           angels.append(angel)

        cv2.putText(frame, text_2, (cX-(int(r)+15),cY-(int(r)+32)) ,cv2.FONT_HERSHEY_SIMPLEX,  0.3,color_2,1,cv2.LINE_AA)
        find_min_max_angel(cX,cY,int_cnt)
        angels.sort ()

        for i in angels[:1] : min_angle=i
        for i in angels[-1:] : max_angle=i
        min_angle=min_angle
        if needle_angel :
              f = collections.Counter(needle_angel)
              needle_angel.sort(key = lambda x:(-f[x], x))
              for i in needle_angel[:1] : needle_angel_=i
       # print(needle_angel_)

  min_value = 0 #usually zero
  max_value = 140
  old_min = min_angle
  old_max = max_angle
  #print(old_min)
  #
  new_min = float(min_value)
  new_max = float(max_value)
  old_value = needle_angel_
  old_range = (old_max - old_min)
  new_range = (new_max - new_min)
  if old_range :
     new_value = (((old_value - old_min) * new_range) / old_range) + new_min
     print(new_value)
     if  len_list and new_value > 0  :
         print(f"Reading of the Gauge is {new_value}")
         (w, h), _ = cv2.getTextSize(
         ("Current Reading: {:4.4f}".format(new_value)+" psi"), cv2.FONT_HERSHEY_SIMPLEX, 0.25, 1)
         #img = cv2.rectangle(frame, (cX-(int(r)+15), cY -(int(r)+30)), (cX  + w, cY-100), (0,255,0), -1)
         draw_text(frame,("Current Reading: {:4.4f}".format(new_value)+" psi"),pos=(cX-(int(r)+12),cY-(int(r)+20)))


  cv2.imshow("frame",frame)
  #cv2.imwrite("frame.jpg",frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
print(angels)
print(min(angels))
print(max(angels))
print(needle_angel_)

vs.release()

cv2.destroyAllWindows()




