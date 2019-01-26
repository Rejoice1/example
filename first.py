import numpy as np
import cv2
import datetime
import time

now = datetime.datetime.now()
n=now.minute

def video():
	cap = cv2.VideoCapture(0)
	now = datetime.datetime.now()

	while(True):
		now = datetime.datetime.now()
		if now.second==59:
			break
    # Capture frame-by-frame
    	ret, frame = cap.read()
    	if ret==true 
       

    # Our operations on the frame come here
        
    	else:    
        	break;

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
while (now.minute==n):


	time.sleep(10)
     video()
     now = datetime.datetime.now()
     n=now.minute
