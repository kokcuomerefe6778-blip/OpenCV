# ORB Dedektörü ve Brute-Force kullanarak 2 resim arası Özellik Eşleştirme (Feature Matching)

import cv2
import numpy as np

yol = "pupy.png"
target_img = cv2.imread(yol, 0)

if target_img is None:
    print("Resim okunamadı! Lütfen dosya yolunu kontrol et.")
else:
    template_img = target_img[100:400, 150:400]
    
    orb = cv2.ORB_create()
    
    kp1, des1 = orb.detectAndCompute(template_img, None)
    kp2, des2 = orb.detectAndCompute(target_img, None)
    
    # 5. Brute-Force Matcher (Kaba Kuvvet Eşleştirici) oluştur
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    
    result_img = cv2.drawMatches(template_img, kp1, target_img, kp2, matches[:30], None, flags=2)
    
    window_name = 'Feature Matching (ORB) - Carpili Kapanis'
    cv2.namedWindow(window_name)
    
    while True:
        cv2.imshow(window_name, result_img)
        if cv2.waitKey(20) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()