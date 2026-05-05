# OpenCV ile diske kayıtlı bir fotoğrafı okuma ve pencerede gösterme

import cv2

# Yolun başına r koyuyoruz ki ters slaşlar (\) ve Türkçe karakterler sorun çıkarmasın
# Dosya adının ve uzantısının (pupy.png) tam doğru olduğundan emin ol!
yol = 'pupy.png'

img = cv2.imread(yol)

# Kontrol mekanizması: Resim gerçekten yüklendi mi?
if img is None:
    print("HATA: Resim bulunamadı. Lütfen dosya adını ve yolunu kontrol et!")
    print("Aranan yol:", yol)
else:
    while True:
        cv2.imshow('Kopek Resmi', img)
        
        # Esc tuşu (27) ile çıkış
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()