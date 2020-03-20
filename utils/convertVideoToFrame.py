import cv2
 
# Opens the Video file
cap= cv2.VideoCapture('Tobii_Videos/kitchen_scene.mp4')
i=0
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i%20 == 0:
        cv2.imwrite("frame_%.4d.jpg" % count, frame)
        count = count + 1
    i+=1
 
cap.release()
cv2.destroyAllWindows()
