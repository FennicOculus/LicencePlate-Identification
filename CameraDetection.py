import cv2
from cv2 import VideoCapture
from datetime import datetime
from CameraVerification import reco

# paused because of hardware problems
def vidRec():
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if vid.isOpened():
        while(True):
            # Capture the video frame
            # by frame
            ret, frame = vid.read()
        
            # Display the resulting frame
            cv2.imshow('Click on V to Verify a car and Q to Quit', frame)
            
            # the 'q' button is set as the
            # quitting button yozu may use any
            # desired button of your choice
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
            #wait for the 'v' bar to take a screenshot 
            if cv2.waitKey(30) & 0xFF == ord('v'):
                print('capturing')
                reco(frame)
                
                
        
        # After the loop release the cap object
        vid.release()
        cv2.destroyAllWindows()
    else:
        print("Error While opening the camera")