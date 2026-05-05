# Haar Cascade XML dosyaları kullanarak Webcam üzerinden Canlı Yüz Tespiti (Face Detection)

import cv2

# OpenCV'nin kendi icindeki hazir egitilmis yuz tanima dosyasini (XML) cekiyoruz
xml_yolu = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml_yolu)

# Webcam'i baslat (0, bilgisayara bagli varsayilan kameradir)
cap = cv2.VideoCapture(0)

window_name = 'Canli Yuz Tespiti - Kapatmak icin ESC veya Carpi'
cv2.namedWindow(window_name)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kameradan goruntu alinamadi!")
        break
        
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3) # Yesil renkli ve 3 kalinliginda cizgi
        
    cv2.imshow(window_name, frame)
    
    if cv2.waitKey(1) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
