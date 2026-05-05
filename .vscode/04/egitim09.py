# Haar Cascade ile sabit bir fotoğraftaki (car_plate.jpg) Rus plakasını tespit edip bulanıklaştırma (Değerlendirme Projesi)

import cv2
import numpy as np

# 1. Resmi oku
img_yolu = "DATA/car_plate.jpg"

# Türkçe karakter sorunu yaşamamak için resmi numpy ile okuyup OpenCV formatına (decode) çeviriyoruz
img_array = np.fromfile(img_yolu, dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

if img is None:
    print("Resim bulunamadı! Lütfen dosya yolunu kontrol et.")
else:
    # 2. Haar Cascade XML dosyasını yükle (Türkçe yol hatası olmaması için OpenCV'nin içindekini çekiyoruz)
    xml_yolu = cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml'
    plate_cascade = cv2.CascadeClassifier(xml_yolu)

    def detect_and_blur_plate(img):
        plate_img = img.copy()
        
        # Plakaları tespit et (scaleFactor ve minNeighbors parametreleri ayarlandı)
        plate_rects = plate_cascade.detectMultiScale(plate_img, scaleFactor=1.3, minNeighbors=3) 
        
        for (x, y, w, h) in plate_rects: 
            # A) Plakanın olduğu bölgeyi (ROI) Numpy dilimleme ile kes
            roi = plate_img[y:y+h, x:x+w]
            
            # B) Kestiğin bölgeyi bulanıklaştır (Notebook'ta 7 verilmiş ama 15 sansürü daha net belli eder)
            blurred_roi = cv2.medianBlur(roi, 15) 
            
            # C) Bulanık bölgeyi orijinal resimdeki yerine geri yapıştır
            plate_img[y:y+h, x:x+w] = blurred_roi
            
        return plate_img

    # 3. Fonksiyonu çalıştır ve sonucu al
    result = detect_and_blur_plate(img)

    # 4. Çarpı tuşuna duyarlı döngü ile ekranda göster
    window_name = 'Proje: Plaka Sansurleme'
    cv2.namedWindow(window_name)
    
    while True:
        cv2.imshow(window_name, result)
        if cv2.waitKey(20) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
            
    cv2.destroyAllWindows()