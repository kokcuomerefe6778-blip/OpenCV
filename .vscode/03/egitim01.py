import cv2
import time

cap = cv2.VideoCapture('../DATA/video_capture.mp4')

fps = 25
if cap.isOpened() == False:
    print("Video dosyası açılırken bir sorun oluştu.")
while cap.isOpened():

    ret, frame = cap.read()
    if ret == True:
        time.sleep(1/ fps)
        if cv2.waitKey(25) & 0xFF == ord('q') or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
            break
    else:
        break     
cap.release()
cv2.destroyAllWindows()


