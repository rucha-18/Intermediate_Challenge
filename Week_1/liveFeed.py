import cv2
cap = cv2.VideoCapture(0)     # Creates VideoCapture object

if not cap.isOpened():
    raise IOError("Camera could not open!")

while True:
    ret,frame = cap.read()      # If frame captured successfully indicated by ret (a boolean value), then store in frame variable
    frame = cv2.resize(frame,None,fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input',frame)
    c = cv2.waitKey(1)
    if c == 27:                    # ASCII value of ESC is 27
        break
cap.release()                       # Closes the webcam
cap.destroyAllWindows()
