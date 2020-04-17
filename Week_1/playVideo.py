import cv2
import numpy as np
cap = cv2.VideoCapture('test.mp4') # Creates video capture object

while(cap.isOpened()):
    ret,frame = cap.read() 
    if ret == True:                 # Indicates whether frame was captures correctly
        cv2.imshow('Frame',frame)
        c = cv2.waitKey(1)
        if c == 27:                 # ASCII value of ESC is 27
            break
    else:
        break
cap.release()                       # Closes the video
cv2.destroyAllWindows()