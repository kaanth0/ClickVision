# 💊 ClickVision

**ClickVision** is a Python-based visual automation bot with a sleek and simple GUI.  
It detects user-defined images on the screen and performs automatic clicks at custom intervals.  
Perfect for repetitive tasks or game automation.  

---

## 🚀 Features
- 🖼️ Upload your own target images easily via GUI  
- 🖱️ Automatically clicks detected images on the screen  
- ⏱️ Customizable click delay for precise timing  
- 💻 Lightweight, responsive, and easy to use  

---

## 🧩 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/kaanth0/ClickVision.git
   cd ClickVision

2. Install dependencies: pip install -r requirements.txt

3. Run the bot: python kaanth0_bot.py

📁 Folder Structure

ClickVision/
│
├── images/              # Uploaded or used reference images
├── kaanth0_bot.py       # Main bot GUI and logic
├── imagesearch.py       # Image detection module (OpenCV-based)
├── requirements.txt     # Dependencies
└── README.md            # Documentation

⚙️ Requirements

keyboard==0.13.5
numpy==2.3.1
opencv_python==4.11.0.86
Pillow==11.3.0
pyautogui==0.9.54

🧠 How It Works

The bot continuously scans your screen for any of the images you upload.
Once a match is found, it automatically moves the cursor to the target location and performs a double-click, waiting for the defined delay before repeating the process.

🧑‍💻 Author

Developed by Kaanth0

If you like this project, consider giving it a ⭐ on GitHub!

---

## 🇹🇷 Türkçe Açıklama

**ClickVision**, sade bir arayüze sahip, Python tabanlı bir görsel otomasyon botudur.  
Ekrandaki kullanıcı tanımlı görselleri algılar ve belirlenen aralıklarla bu görsellere otomatik olarak tıklama işlemi yapar.  
Tekrarlayan görevler, oyun otomasyonları veya test süreçleri için idealdir.  

---

### 🚀 Özellikler
- 🖼️ Arayüz üzerinden kolayca hedef görsel yükleme  
- 🖱️ Yüklenen görselleri ekranda algılayıp otomatik tıklama  
- ⏱️ Tıklama aralığını kişiselleştirme  
- 💻 Hafif, sade ve hızlı çalışma yapısı  

---

### 🧩 Kurulum
1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/kaanth0/ClickVision.git
   cd ClickVision

2. Gerekli kütüphaneleri yükleyin: pip install -r requirements.txt

3. Botu çalıştırın: python kaanth0_bot.py

⚙️ Gereksinimler

keyboard==0.13.5
numpy==2.3.1
opencv_python==4.11.0.86
Pillow==11.3.0
pyautogui==0.9.54

🧠 Nasıl Çalışır

Bot, ekranı sürekli olarak tarar ve yüklediğiniz görsellerden biri ekranda belirdiğinde otomatik olarak tıklama işlemi yapar.
Tıklama aralıkları ve bekleme süreleri kullanıcı tarafından arayüz üzerinden ayarlanabilir.

🧑‍💻 Geliştirici

Geliştiren: Kaanth0

Projeyi beğendiysen bir ⭐ bırakmayı unutma 😊

- Metin2 nelerle uğraştırıyorsun beni -
- Metin2 için kullanacak arkadaşlara bazı AC'ler opencv yi yakalıyor dikkat
