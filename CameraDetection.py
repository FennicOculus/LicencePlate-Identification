import cv2
from cv2 import VideoCapture
# paused because of hardware problems
cv2.namedWindow("preview")
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if vid.isOpened():
    while(True):
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button yozu may use any
        # desired button of your choice
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    cv2.destroyAllWindows()
else:
    print("Error")