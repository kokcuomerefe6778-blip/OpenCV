import cv2
import numpy as np

yol = r"C:\yazilim\OpenCV\pupy.png"
img1 = cv2.imread(yol)

if img1 is None:
    print("Resim bulunamadı.")
else:
    img1 = cv2.resize(img1, (600, 600))
    img2 = np.zeros((600,600, 3), dtype= np.uint8)
    img2[:] = (255, 0, 0)

    blended = cv2.addWeighted(src1=img1, alpha=0.7, src2=img2, beta=0.3, gamma=0)
    cv2.imshow("Orjinal", img1)
    cv2.imshow("Harmanlanmis - Gece Gorus Filtresi", blended)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


