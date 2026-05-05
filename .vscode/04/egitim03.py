# Dış Hat / Kontur Algılama (Contour Detection) ile resimdeki nesnelerin sınırlarını çizme

import cv2
import numpy as np

yol = "pupy.png"
img = cv2.imread(yol)

if img is None:
    print("Resim okunamadı! Lütfen dosya yolunu kontrol et.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray, 100, 200)
    
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
   
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    
    window_name = 'Kontur Algilama - Carpili Kapanis'
    cv2.namedWindow(window_name)
    
    while True:
        cv2.imshow(window_name, contour_img)
        
        if cv2.waitKey(1) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
            
    cv2.destroyAllWindows()
