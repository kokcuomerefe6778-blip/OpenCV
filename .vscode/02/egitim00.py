import cv2
import numpy as np

yol = r"C:\yazilim\OpenCV\pupy.png"
img_bgr = cv2.imread(yol)

if img_bgr is None:
    print("Resim bulunamadı.")
else:
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    cv2.imshow("Orjinal Resim", img_bgr)
    cv2.imshow("HSV Resim", img_hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()