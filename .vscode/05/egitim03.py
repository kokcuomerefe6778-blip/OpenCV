import cv2
import sys

def ask_for_tracker():
    print("Harika! Hangi takip algoritmasını (Tracker) kullanmak istersin?")
    print("0 - BOOSTING (Eski ama temel bir algoritma)")
    print("1 - MIL      (Daha isabetli ama yavaş)")
    print("2 - KCF      (Hızlı ve isabetli - TAVSİYE EDİLEN)")
    print("3 - TLD      (Hatalardan iyi geri döner ama çok yanlış alarm verir)")
    print("4 - MEDIANFLOW (Çok tahmin edilebilir/yumuşak hareketler için iyi)")
    
    choice = input("Lütfen takip algoritmasını seçin (0-4): ")
    
    # OpenCV'nin yeni sürümlerinde bazı algoritmalar legacy (eski) kısmına taşındı.
    # Çökmemesi için sürüm kontrolünü try-except ile yapıyoruz.
    try:
        if choice == '0':
            tracker = cv2.legacy.TrackerBoosting_create()
            name = "BOOSTING"
        elif choice == '1':
            tracker = cv2.TrackerMIL_create()
            name = "MIL"
        elif choice == '2':
            tracker = cv2.TrackerKCF_create()
            name = "KCF"
        elif choice == '3':
            tracker = cv2.legacy.TrackerTLD_create()
            name = "TLD"
        elif choice == '4':
            tracker = cv2.legacy.TrackerMedianFlow_create()
            name = "MEDIANFLOW"
        else:
            print("Geçersiz seçim! KCF varsayılan olarak seçildi.")
            tracker = cv2.TrackerKCF_create()
            name = "KCF"
    except AttributeError:
        # Eğer OpenCV eski bir sürümse (3.x veya 4.0-4.4 arası)
        if choice == '0': tracker = cv2.TrackerBoosting_create(); name = "BOOSTING"
        elif choice == '1': tracker = cv2.TrackerMIL_create(); name = "MIL"
        elif choice == '2': tracker = cv2.TrackerKCF_create(); name = "KCF"
        elif choice == '3': tracker = cv2.TrackerTLD_create(); name = "TLD"
        elif choice == '4': tracker = cv2.TrackerMedianFlow_create(); name = "MEDIANFLOW"
        else: tracker = cv2.TrackerKCF_create(); name = "KCF"

    return tracker, name

# Tracker'ı ve ismini al
tracker, tracker_name = ask_for_tracker()

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("Kameradan görüntü alınamadı!")
    sys.exit() # sys kutuphanesini burada programi guvenli sekilde kapatmak icin kullandik

print("Lütfen açılan pencerede fare ile takip edilecek nesneyi seçin.")
print("Seçimi onaylamak için BOŞLUK (SPACE) veya ENTER tuşuna basın.")
roi = cv2.selectROI(tracker_name, frame, False)

ret = tracker.init(frame, roi)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    success, roi = tracker.update(frame)
    
    if success:
        (x, y, w, h) = tuple(map(int, roi))
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    else:
        cv2.putText(frame, "Takip Kaybedildi!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.putText(frame, tracker_name, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.imshow(tracker_name, frame)

    if cv2.waitKey(1) == 27 or cv2.getWindowProperty(tracker_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
