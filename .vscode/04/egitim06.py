# Fare (Mouse) ile özel renkler/tohumlar belirleyerek manuel Watershed Görüntü Bölütleme

import cv2
import numpy as np

yol = "pupy.png"
road = cv2.imread(yol)

if road is None:
    print("Resim okunamadı! Lütfen dosya yolunu kontrol et.")
    exit()

road_copy = road.copy()

# Boş bir işaretçi (marker) matrisi (Watershed algoritması bununla beslenir)
marker_image = np.zeros(road.shape[:2], dtype=np.int32)
# Ekranda sonuçları göreceğimiz renkli matris
segments = np.zeros(road.shape, dtype=np.uint8)

colors = [
    (0, 0, 0),       # 0: Siyah (Arka plan/Bilinmeyen)
    (255, 0, 0),     # 1: Mavi
    (0, 255, 0),     # 2: Yeşil
    (0, 0, 255),     # 3: Kırmızı
    (255, 255, 0),   # 4: Camgöbeği (Cyan)
    (255, 0, 255),   # 5: Eflatun (Magenta)
    (0, 255, 255),   # 6: Sarı
    (128, 0, 0),     # 7: Koyu Mavi
    (0, 128, 0),     # 8: Koyu Yeşil
    (0, 0, 128)      # 9: Koyu Kırmızı
]

current_marker = 1
marks_updated = False


def mouse_callback(event, x, y, flags, param):
    global marks_updated
    
    
    if event == cv2.EVENT_LBUTTONDOWN or (event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON):
        
        cv2.circle(marker_image, (x, y), 5, current_marker, -1)
        
        cv2.circle(road_copy, (x, y), 5, colors[current_marker], -1)
        marks_updated = True

cv2.namedWindow('Orijinal Resim (Buraya Ciz)')
cv2.setMouseCallback('Orijinal Resim (Buraya Ciz)', mouse_callback)

while True:
    cv2.imshow('Watershed Sonuclari', segments)
    cv2.imshow('Orijinal Resim (Buraya Ciz)', road_copy)
    
    k = cv2.waitKey(1)
    
    if k == 27 or cv2.getWindowProperty('Orijinal Resim (Buraya Ciz)', cv2.WND_PROP_VISIBLE) < 1:
        break
    elif k == ord('c'): # 'C' tuşuna basılırsa ekranı temizle
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.uint8)
    elif k > 0 and chr(k).isdigit(): # 0-9 arası bir tuşa basılırsa rengi değiştir
        current_marker = int(chr(k))
        
    
    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)
        segments = np.zeros(road.shape, dtype=np.uint8)
        for color_ind in range(10):
            segments[marker_image_copy == color_ind] = colors[color_ind]
        marks_updated = False
        
cv2.destroyAllWindows()
