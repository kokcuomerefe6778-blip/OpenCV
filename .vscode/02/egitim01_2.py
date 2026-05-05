import cv2
import numpy as np

yol = r"C:\yazilim\OpenCV\pupy.png"
img1 = cv2.imread(yol)

if img1 is None:
    print("Resim bulunamadı.")
else:
    img1 = cv2.resize(img1, (600,600))
    img2_logo = np.zeros((200,200,3), dtype=np.uint8)
    cv2.circle(img2_logo, (100,100), 80,( 0,255,0),-1)

    roi = img1[400:600, 400:600]

    img2gray = cv2.cvtColor(img2_logo, cv2.COLOR_BGR2GRAY)
    _,mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_arkaplan = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img2_onplan = cv2.bitwise_and(img2_logo, img2_logo, mask=mask)

    hedes_bolge = cv2.add(img1_arkaplan, img2_onplan)

    cv2.imshow("Kopegi oyduk",img1_arkaplan)
    cv2.imshow("Birleştirdik", hedes_bolge)
    cv2.imshow("FINAL", img1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
