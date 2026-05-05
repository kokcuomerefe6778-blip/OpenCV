import cv2
import numpy as np

yol = r"C:\yazilim\OpenCV\pupy.png"
img = cv2.imread(yol, 0)

if img is None:
    print("Resim bulunamadı")
else:
    ret, th1_binary = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)
    ret, th2_binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, th3_trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    th4_adaptive_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
    th5_adaptive_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 8)

    pencere_orjinal = "1- Orijinal (Gri)"
    pencere_binary = "2- Binary"
    pencere_adaptive = "3- Adaptive Mean" 
    
    cv2.namedWindow(pencere_orjinal)
    cv2.namedWindow(pencere_binary)
    cv2.namedWindow(pencere_adaptive)

    cv2.imshow(pencere_orjinal, img)
    cv2.imshow(pencere_binary, th1_binary)
    cv2.imshow(pencere_adaptive, th4_adaptive_mean)
    
cv2.waitKey(0)
cv2.destroyAllWindows()