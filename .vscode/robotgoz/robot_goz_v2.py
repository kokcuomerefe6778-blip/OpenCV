import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()
    if not ret:
        break
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    alt_kirmizi = np.array([160, 100, 100])
    ust_kirmizi = np.array([180, 255, 255])

    maske = cv2.inRange(hsv_frame, alt_kirmizi, ust_kirmizi)
    maske = cv2.erode(maske, None, iterations=2)
    maske = cv2.dilate(maske, None, iterations=2)

    contours, _ = cv2.findContours(maske, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        alan = cv2.contourArea(cnt)
        if alan > 500:
            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x, y) ,( x + w, y + h), (0, 255, 0), 2)

            merkez_x = int(x + w /2 )
            merkez_y = int(y + h /2 )
            cv2.circle(frame, (merkez_x, merkez_y), 5, (255, 0, 0), -1)

            yazi = "Hedef X:" + str(merkez_x) + "Y:" + str(merkez_y)
            cv2.putText(frame, yazi, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow("Robotun Gozu - Hedef Takibi", frame)
    cv2.imshow("Karanlik Maske", maske)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()        