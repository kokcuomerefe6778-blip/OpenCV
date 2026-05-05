# Şablon Eşleştirme (Template Matching) ile büyük resim içinde küçük bir nesneyi/şablonu arama

import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# 1. Büyük resmi ve aranacak şablonu (yüzü) okuyup RGB formatına çeviriyoruz
full = cv2.imread('pupy.png')
if full is None:
    print("HATA: 'pupy.png' bulunamadı! Lütfen dosya yolunu kontrol edin.")
    sys.exit()
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)

face = cv2.imread('pupy_face.png')
if face is None:
    print("HATA: 'pupy_face.png' bulunamadı!")
    print("Lütfen köpeğin yüzünü kırpıp 'pupy_face.png' adıyla ana klasöre kaydettiğinizden emin olun.")
    sys.exit()
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

# Şablonun genişlik (width) ve yüksekliğini (height) alıyoruz ki dikdörtgeni çizebilelim
height, width, channels = face.shape

# OpenCV'nin sunduğu 6 farklı şablon eşleştirme metodunun listesi
methods = [
    'cv2.TM_CCOEFF', 
    'cv2.TM_CCOEFF_NORMED', 
    'cv2.TM_CCORR',
    'cv2.TM_CCORR_NORMED', 
    'cv2.TM_SQDIFF', 
    'cv2.TM_SQDIFF_NORMED'
]

# Her bir metot için döngüye giriyoruz
for m in methods:
    
    # Her çizim işleminden önce orijinal büyük resmin temiz bir kopyasını oluşturuyoruz
    full_copy = full.copy()
    
    # String ismini ('cv2.TM_CCOEFF' gibi) çalışan bir Python koduna dönüştürüyoruz
    method = eval(m)

    # Şablon Eşleştirme (Template Matching) fonksiyonunu uyguluyoruz
    res = cv2.matchTemplate(full_copy, face, method)
    
    # Benzerlik haritasındaki en düşük ve en yüksek değerleri ve bunların koordinatlarını alıyoruz
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # Eğer metot SQDIFF ise (fark hesabı yapıyorsa) en düşük değere sahip koordinatı başlangıç noktası seç
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc    
    # Diğer (benzerlik hesabı yapan) metotlar için en yüksek değere sahip koordinatı seç
    else:
        top_left = max_loc
            
    # Dikdörtgenin sağ alt köşesini, sol üst köşeye şablonun genişlik ve yüksekliğini ekleyerek buluyoruz
    bottom_right = (top_left[0] + width, top_left[1] + height)

    # Bulunan noktaya kırmızı (RGB: 255,0,0) renkli kalın bir dikdörtgen çiziyoruz
    cv2.rectangle(full_copy, top_left, bottom_right, color=(255, 0, 0), thickness=10)

    # Sonuçları yan yana iki grafik olarak ekrana çizdiriyoruz
    fig = plt.figure(figsize=(10, 5))
    
    # Çarpı (X) tuşuna basıldığında tüm döngüyü ve programı anında kapatacak olay
    def on_close(event):
        os._exit(0)
    fig.canvas.mpl_connect('close_event', on_close)

    # Soldaki Grafik: Eşleşme Benzerlik (Isı) Haritası
    plt.subplot(121)
    plt.imshow(res, cmap='gray')
    plt.title('Result of Template Matching')
    
    # Sağdaki Grafik: Bulunan Yerin Dikdörtgen İçinde Gösterimi
    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('Detected Point')
    
    plt.suptitle(m) # Üst başlığa kullanılan metodun adını yazıyoruz
    plt.show() 