import cv2
cap = cv2.VideoCapture("D:/All/Projects/Albumcover/videos/clipsix.mp4")
property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
length = int(cv2.VideoCapture.get(cap, property_id))
print(length)