import os
import cv2
import numpy as np


def get_vh_lines(img,image_path):
    if (img is None) :
        print(f"{image_path} this is incorrect no img found")
    else:
       
        # converting img to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imwrite(f'./output/opencv/gray{i}.jpeg', gray)
    
        # splits the image and clahe 
        # C – Contrast
        # L – Limited
        # A – Adaptive
        # H – Histogram
        # E – Equalization
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        gray_clahe = clahe.apply(gray)    
        # cv2.imwrite(f'./output/opencv/gray_clahe{i}.jpeg', gray_clahe)
        
        # Better threshold (adaptive handles uneven lighting)
        thresh = cv2.adaptiveThreshold(
            gray_clahe, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY_INV,
            15, 10
        )
         
        
        # --- Horizontal lines ---
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60,1))
        horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel)
        # cv2.imwrite(f'./output/opencv/horizontal{i}.jpeg', horizontal)
        
        # connect broken horizontal lines
        horizontal = cv2.dilate(horizontal, np.ones((2,2),np.uint8), iterations=3)
        # cv2.imwrite(f'./output/opencv/horizontal_dilated{i}.jpeg', horizontal)
        
        # --- Vertical lines ---
        vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,60))
        vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel)
        # cv2.imwrite(f'./output/opencv/vertical{i}.jpeg', vertical)
         
        # connect broken vertical lines
        vertical = cv2.dilate(vertical, np.ones((2,2),np.uint8), iterations=3)
        
        # cv2.imwrite(f'./output/opencv/vertical_dilate{i}.jpeg', vertical)
        # h_img_path=f'D:/Anuj_S_Jain/Data/Code/Project/Society_MCE_QT/Society_MCE/Prototype/output/opencv/horizontal_dilated{i}.jpeg'
        # h_img = cv2.imread(h_img_path)

        return horizontal,vertical

def get_h_counters(horizontal):
    contours_h, _ = cv2.findContours(horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours_h
def get_v_counters(vertical):
    contours_v, _ = cv2.findContours(vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours_v

def get_h_angle(contours_h):
    angle_arr=[]
    for counter in contours_h:
        vx, vy, x0, y0 = cv2.fitLine(counter, cv2.DIST_L2, 0, 0.01, 0.01)
        angle = np.arctan2(vy, vx)
        rotation_angle =np.degrees(angle)
        angle_arr.append(rotation_angle)
    return angle_arr
    
def get_v_angle(contours_v):
    angle_arr=[]
    for counter in contours_v:
        vx, vy, x0, y0 = cv2.fitLine(counter, cv2.DIST_L2, 0, 0.01, 0.01)
        angle = np.arctan2(vy, vx)
        rotation_angle =np.degrees(angle)
        angle_arr.append(rotation_angle)
    return angle_arr

def rotate_angle_avg(angle_arr):
    rotation_angle_avg=float(sum(angle_arr)/len(angle_arr))
    return rotation_angle_avg

def rotate_img(img,rotation_angle_avg):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    img_matrix = cv2.getRotationMatrix2D(center, rotation_angle_avg, 1.0)
    rotated_img = cv2.warpAffine(img, img_matrix, (w, h))
    return rotated_img

def rotation_correct_img(image_path):
    if not os.path.exists(image_path):
        print(f"{image_path} Path not found")
        return None

    img = cv2.imread(image_path)

    if img is None:
        print(f"{image_path} Image not found")
        return None
    else:
        horizontal,vertical=get_vh_lines(img,image_path)
        if len(horizontal) >= len(vertical):
            contours_h=get_h_counters(horizontal)
            angle_arr_h=get_h_angle(contours_h)
            rotation_angle_avg=rotate_angle_avg(angle_arr_h)
            rotated_img=rotate_img(img,rotation_angle_avg)
            return rotated_img
        elif len(horizontal) < len(vertical):
            contours_v=get_v_counters(vertical)
            angle_arr_v=get_v_angle(contours_v)
            rotation_angle_avg=rotate_angle_avg(angle_arr_v)
            rotated_img=rotate_img(img,-rotation_angle_avg)
            return rotated_img
        elif len(horizontal) == 0 or len(vertical):
            pass
        
    