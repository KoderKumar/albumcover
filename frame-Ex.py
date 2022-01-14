import cv2
import random
import math

#rand = random.randint(6000,16000)
cap= cv2.VideoCapture('D:/All/Projects/Albumcover/videos/clipsix.mp4')
i=1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i%200 == 0:
        cv2.imwrite('clipframe'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()