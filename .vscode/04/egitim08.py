# Haar Cascade ile Webcam'den Rus plakalarını tespit edip otomatik bulanıklaştırma (Sansürleme)

import cv2

xml_yolu = cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml'
plate_cascade = cv2.CascadeClassifier(xml_yolu)


cap = cv2.VideoCapture(0)

window_name = 'Canli Plaka Sansurleme'
cv2.namedWindow(window_name)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, 1.2, 5)
    
    for (x, y, w, h) in plates:
        roi = frame[y:y+h, x:x+w]
        frame[y:y+h, x:x+w] = cv2.medianBlur(roi, 35)
        
    cv2.imshow(window_name, frame)
    
    # Video aktığı için waitKey(1) olmak ZORUNDA. Çarpıya basınca kapanması için de getWindowProperty kontrolü yapıyoruz.
    if cv2.waitKey(1) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()