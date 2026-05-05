# Canny Algoritması ile Kenar Algılama (Edge Detection) ve medyan tabanlı dinamik eşikleme

import cv2
import numpy as np

yol = "pupy.png"
img = cv2.imread(yol)

if img is None:
    print("Resim yok!")
else:
    med_val = np.median(img)
    lower = int(max(0, 0.7 * med_val))
    upper = int(min(255, 1.3 * med_val))
    blurred_img = cv2.blur(img, ksize=(5, 5))
    edges = cv2.Canny(blurred_img, threshold1=lower, threshold2=upper + 50)
    window_name = 'Canny Kenar Algılama'
    cv2.namedWindow(window_name)
    
    while True:
        cv2.imshow(window_name, edges)
        if cv2.waitKey(20) == 27 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()
