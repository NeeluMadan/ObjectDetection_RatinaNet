import os
import cv2
import glob
import numpy as np
 
img_array = []
for filename in sorted(glob.glob('kitchen_scene/*.jpg')):
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
out = cv2.VideoWriter('Tobii_Videos/kitchen_scene.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
