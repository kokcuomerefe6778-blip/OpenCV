# Fare olayları (Mouse Callback) kullanarak resim üzerinde fare ile dinamik dikdörtgen çizme

import cv2
import numpy as np

drawing = False 
ix,iy = -1, -1

def draw_rectangle(event,x,y,flags,param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy= x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        # Parmağını sol tıktan çekince çizim biter
        drawing = False
        # Son dikdörtgeni tamamla
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

# DİKKAT: uint16 yerine uint8 yaptık ki renkler bozulmasın
img = np.zeros((512,512,3), np.uint8)

# Pencereyi isimlendir
cv2.namedWindow(winname='my_drawing')

# Fare tıklamalarını fonksiyonumuza bağla
cv2.setMouseCallback('my_drawing', draw_rectangle)

while True: 
    cv2.imshow('my_drawing', img)
    
    # 1. Fareyi okuması ve pencerenin donmaması için tek başına bırakıyoruz:
    cv2.waitKey(1) 
        
    # 2. SADECE ÇARPI (X) İLE KAPATMA KONTROLÜ:
    if cv2.getWindowProperty('my_drawing', cv2.WND_PROP_VISIBLE) < 1:
        break

# Program bitince tüm pencereleri temizle
cv2.destroyAllWindows()