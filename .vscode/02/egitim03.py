import cv2
import numpy as np

yol = r"C:\yazilim\OpenCV\pupy.png" 
img = cv2.imread(yol)

if img is None:
    print("Resim bulunamadı.")
else:
    img = cv2.resize(img, (400, 400))

    cv2.putText(img, text='PUPPY', org=(10, 350), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=(0, 0, 255), thickness=3)
    
    blur_avg = cv2.blur(img, ksize=(5, 5))
    blur_gauss = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=0)
    blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    gurultulu_img = img.copy()
    rastgele_matris = np.random.rand(*img.shape[:2])
    gurultulu_img[rastgele_matris < 0.05] = [255, 255, 255]

    blur_median = cv2.medianBlur(gurultulu_img, 5)

    cv2.imshow("1 - Orijinal", img)
    cv2.imshow("2 - Gaussian Blur (Dogal)", blur_gauss)
    cv2.imshow("3 - Bilateral Blur (Yazi kenari bozulmadi!)", blur_bilateral)
    
    cv2.imshow("4 - Gurultulu (Bozuk) Resim", gurultulu_img)
    cv2.imshow("5 - Median Blur (Gurultu Silindi!)", blur_median)

    
cv2.waitKey(0)
cv2.destroyAllWindows()