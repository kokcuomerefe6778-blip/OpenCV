import cv2
import numpy as np

yol = r"C:\yazilim\OpenCV\pupy.png" 
img = cv2.imread(yol)

if img is None:
    print("Resim yok!")
else:
    # FARE FONKSİYONU: Artık SOL TIK (LBUTTONDOWN) ile çalışacak!
    def draw_circle(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN: 
            # (x, y) merkezli, 100 yarıçaplı, tam kırmızı daire
            cv2.circle(img, (x, y), 100, (0, 0, 255), -1)

    cv2.namedWindow(winname='pencere')
    cv2.setMouseCallback('pencere', draw_circle)

    while True: 
        cv2.imshow('pencere', img)
        
        if cv2.waitKey(20) & 0xFF == 27:
            break
            
        if cv2.getWindowProperty('pencere', cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()