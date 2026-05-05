# Watershed (Su Ayrımı) Algoritması ile birbirine değen/yapışık nesneleri ayırma

import cv2
import numpy as np

yol = "pupy.png"
img = cv2.imread(yol)

if img is None:
    print("Resim okunamadı! Lütfen dosya yolunu kontrol et.")
else:
    
    result_img = img.copy()

    blurred = cv2.medianBlur(img, 15)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    markers = cv2.watershed(img, markers)
    result_img[markers == -1] = [0, 0, 255]

    window_name = 'Watershed Algoritmasi - Birbirine Degen Nesneleri Ayirma'
    cv2.namedWindow(window_name)
    while True:
        cv2.imshow(window_name, result_img)
        if cv2.waitKey(20) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()
