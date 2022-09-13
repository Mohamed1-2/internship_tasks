import numpy as np
import cv2
from imutils import perspective
import imutils
import pandas as pd
import math

def gauge_edges(c_col,c_row,circ_radius,frame):
    separation= 10 #in degrees
    interval = int(360/separation)
    p1 = np.zeros((interval,2))  #set empty arrays
    p2 = np.zeros((interval,2))
    p_text = np.zeros((interval,2))

    for i in range(0,interval):
        for j in range(0,2):
            if (j%2==0):
                p1[i][j] = c_col + 0.8 * circ_radius * np.cos(separation * i * np.pi / 180) #point for lines
            else:
                p1[i][j] = c_row + 0.8 * circ_radius * np.sin(separation * i * np.pi / 180)

    text_offset_x = 10
    text_offset_y = 5
    for i in range(0, interval):
        for j in range(0, 2):
            if (j % 2 == 0):
                p2[i][j] = c_col + circ_radius * np.cos(separation * i * np.pi / 180)
                p_text[i][j] = c_col - text_offset_x + 1.2 * circ_radius * np.cos((separation) * (i+9) * np.pi / 180) #point for text labels, i+9 rotates the labels by 90 degrees
            else:
                p2[i][j] = c_row + circ_radius * np.sin(separation * i * np.pi/ 180)
                p_text[i][j] = c_row + text_offset_y + 1.2* circ_radius * np.sin((separation) * (i+9) * np.pi / 180)  # point for text labels, i+9 rotates the labels by 90 degrees

    #add the lines and labels to the image
    for i in range(0,interval):
        cv2.line(frame, (int(p1[i][0]), int(p1[i][1])), (int(p2[i][0]), int(p2[i][1])),(0, 255, 0), 2)
        cv2.putText(frame, '%s' %(int(i*separation)), (int(p_text[i][0]), int(p_text[i][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.2,(0, 255, 0),1,cv2.LINE_AA)

def convert_img_to_BGR(frame):
    # Make float and divide by 255 to give BGRdash
    bgrdash = frame.astype(np.float)/255.
    # Calculate K as (1 - whatever is biggest out of bgrFloat)
    K = 1 - np.max(bgrdash, axis=2)
    # re-scale the Channel back up to uint8
    K = (K * 255).astype(np.uint8)

    return K





def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    # set bg label to black
    labeled_img[label_hue==0] = 0
    plt.imshow(labeled_img)
    cv2.waitKey()


def plt_imshow(title, image):
    # convert the image frame BGR to RGB color space and display it
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	plt.imshow(image)
	plt.title(title)
	plt.grid(False)
	plt.show()

def region_of_interest(img, vertices):
    mask= np.zeros_like(img)
    match_mask_color= 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image= cv2.bitwise_and(img, mask)
    return masked_image

def find_min_max_angel(x,y,list_Contours):
    frth_quad_index=[]
    thrd_quad_index=[]
    reference_zero_angle= 20
    reference_end_angle= 330
    min_angle=90
    max_angle=270
    angels=[]

    for i in range(len(list_Contours)):
            a= list_Contours[i]
            a= a.reshape(len(a),2)
            a= pd.DataFrame(a)
            x1= a.iloc[:,0].mean()
            y1= a.iloc[:,1].mean()
            #print("x1",x1)
           # print("y1",y1)
            xlen= x1-x
            ylen= y-y1

            #Taking arc-tan of ylen/xlen to find the angle
            res= np.arctan(np.divide(float(ylen), float(xlen)))
            res= np.rad2deg(res)

def dist_2_pts(x1, y1, x2, y2):
    #print np.sqrt((x2-x1)^2+(y2-y1)^2)
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def get_contour_areas(contours):

        all_areas= []

        for cnt in contours:
            area= cv2.contourArea(cnt)
            all_areas.append(area)

        return all_areas
def midpoint(ptA, ptB):
   return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
def most_frequent(List):
    return max(set(List), key = List.count)
def draw_text(img, text,
          font=cv2.FONT_HERSHEY_SIMPLEX,
          pos=(0, 0),
          font_scale=1,
          font_thickness=1,
          text_color=(0, 0, 0),
          text_color_bg=(0, 255, 0)
          ):

    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.rectangle(img, pos, (x + text_w-325, y + text_h-32), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h-24 + font_scale - 1), font, font_scale -0.7, text_color, font_thickness)

    return text_size
def adjust_gamma(img,gamma=1.0):
    # build lookup tabla mapping the pixal values [0,255]
    # thier adjusted gamma values
    invGamma = 1.0/gamma
    table = np.array([((i/255.0)** invGamma)*255
        for i in np.arange(0,256)]).astype("uint8")
    return cv2.LUT(img, table)

