import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
while True:
    ret , frame = kamera.read()
    if not ret:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    alt_kirmizi = np.array([160,100, 100])
    ust_kirmizi = np.array([180,255,255])

    maske = cv2.inRange(hsv_frame, alt_kirmizi, ust_kirmizi)

    cv2.imshow("Orjinal Kamera", frame)
    cv2.imshow("Sadece Kırmızı", maske)

    if cv2.waitKey(1) & 0xFF == ord("q"):       
        break

kamera.release()
cv2.destroyAllWindows() 