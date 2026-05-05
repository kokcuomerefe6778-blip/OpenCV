# 🚀 OpenCV Görüntü İşleme Eğitim Serisi ve Projeleri

Bu depo, Python ve OpenCV kütüphanesi kullanılarak sıfırdan bilgisayarlı görü (Computer Vision) tekniklerinin öğrenilmesi ve uygulanması amacıyla oluşturulmuştur. 

İçerisinde temel görüntü okuma işlemlerinden, nesne takibine; yapay zeka (Haar Cascade) destekli canlı yüz tespitinden, otomatik plaka sansürleme gibi mini projelere kadar pek çok farklı çalışma bulunmaktadır.

---

## 📋 İçindekiler / Çalışmalar

### 🔹 Temel Seviye Görüntü İşlemleri
* **`01/egitim2.py`**: OpenCV ile temel görüntü okuma (imread), ekranda gösterme (imshow) ve güvenli çıkış işlemleri.
* **`01/egitim3-2.py`**: OpenCV Fare (Mouse Callback) olayları kullanılarak resim üzerinde farenin sürüklenmesiyle dinamik çizimler yapma.

### 🔹 İleri Seviye Görüntü İşleme ve Analiz
* **`04/egitim01.py`**: Şablon Eşleştirme (Template Matching) ile büyük bir resim içinde küçük bir nesneyi/şablonu otomatik arama ve işaretleme.
* **`04/egitim02.py`**: Canny Algoritması kullanılarak resimlerde Kenar Algılama (Edge Detection) ve Medyan tabanlı dinamik eşik (threshold) belirleme.
* **`04/egitim03.py`**: Kontur (Dış Hat) Algılama (Contour Detection) ile resimdeki nesnelerin sınırlarını algılayıp çizdirme.
* **`04/egitim04.py`**: ORB Dedektörü ve Brute-Force Matcher kullanarak iki farklı resim arasında Özellik Eşleştirme (Feature Matching).
* **`04/egitim05.py`**: Watershed (Su Ayrımı) Algoritması ile birbirine değen/yapışık nesneleri (bozuk para, hücre vb.) otomatik olarak ayırma.
* **`04/egitim06.py`**: Fare (Mouse) ile özel renkler ve tohumlar (seed) belirleyerek manuel Watershed Görüntü Bölütleme (Image Segmentation) yapma.

### 🔹 Uygulamalı Projeler (Haar Cascades)
* **`04/egitim07.py`**: Bilgisayarın kamerasını (Webcam) kullanarak gerçek zamanlı Canlı Yüz Tespiti (Face Detection).
* **`04/egitim08.py`**: Webcam üzerinden canlı olarak okunan videodaki Rus plakalarını tespit edip otomatik bulanıklaştırma (Canlı Sansürleme).
* **`04/egitim09.py`**: Değerlendirme Projesi: Sabit bir fotoğraftaki (car_plate.jpg) plakayı tespit edip sadece o bölgeyi bulanıklaştırma (ROI - Region of Interest işlemleri).

---

## ⭐ Öne Çıkan Özellikler

Bu repodaki kodlar, standart OpenCV eğitim kodlarından farklı olarak kullanım kolaylığı sağlayacak şekilde optimize edilmiştir:

1. **Kusursuz Pencere Kapatma (X Tuşu Desteği):** OpenCV'nin klasikleşmiş "çarpı tuşuna basınca pencerenin donma/kapanmama" sorunu `cv2.getWindowProperty` fonksiyonu ile tamamen çözülmüş, tüm scriptler Windows standartlarına uygun şekilde çarpıdan kapanabilir hale getirilmiştir.
2. **Türkçe Karakter Desteği:** `cv2.imread` fonksiyonunun Türkçe karakterli klasör isimlerinde çökmesi sorunu, `Numpy` raw bytestream okuma (`np.fromfile` & `cv2.imdecode`) yöntemiyle kalıcı olarak çözülmüştür.
3. **Temiz Döngüler:** Mümkün olan her yerde gereksiz işlemci tüketiminden kaçınılmış, statik fotoğraflar için sadece klavye/fare bekleyen sade komutlar tercih edilmiştir.

---

## ⚙️ Kurulum ve Gereksinimler

Bu projedeki kodları kendi bilgisayarınızda çalıştırabilmek için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

```bash
pip install opencv-python numpy matplotlib
```

**Not:** Projedeki dosya yolları bağıl yol (relative path) olarak ayarlanmıştır. Projeyi bilgisayarınıza indirip terminalde ana klasörden çalıştırdığınızda (kullanılan `pupy.png` veya `DATA/` gibi kaynakların ana dizinde olması koşuluyla) kodların içerisine girip bir ayar yapmanıza gerek kalmadan "tak-çalıştır" şeklinde sorunsuz çalışacaktır.

---
