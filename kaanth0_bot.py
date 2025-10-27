import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import threading
import time
from PIL import Image
from imagesearch import imagesearch
import os
import shutil

class Kaanth0Bot:
    def __init__(self):
        self.running = False
        self.click_delay = 1
        self.bot_thread = None
        self.last_click_time = None

        # 📁 Proje dizini ve images klasörü
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_dir = os.path.join(self.base_dir, "images")
        os.makedirs(self.image_dir, exist_ok=True)

        # GUI Başlat
        self.root = tk.Tk()
        self.root.title("Kaanth0")
        self.root.geometry("400x500")
        self.root.configure(bg="#1a1a1a")
        self.root.resizable(False, False)

        self.image_paths = []
        self.setup_gui()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def setup_gui(self):
        # Başlık
        tk.Label(
            self.root,
            text="💊 Kaanth0 💊",
            font=("Segoe UI Black", 20, "bold"),
            fg="#00ff88",
            bg="#1a1a1a"
        ).pack(pady=15)

        # Ayarlar çerçevesi
        settings_frame = tk.Frame(self.root, bg="#222", bd=2, relief="ridge")
        settings_frame.pack(padx=20, pady=15, fill=tk.X)

        tk.Label(settings_frame, text="Tıklama Aralığı (saniye):", bg="#222", fg="#fff").grid(row=0, column=0, sticky="w", pady=5)
        self.click_delay_entry = tk.Entry(settings_frame, width=7, bg="#333", fg="#00ff88", insertbackground="#00ff88", justify="center", relief="flat")
        self.click_delay_entry.insert(0, str(self.click_delay))
        self.click_delay_entry.grid(row=0, column=1, padx=8)

        # Durum
        self.status_label = tk.Label(self.root, text="Durum: Kapalı", bg="#1a1a1a", fg="#ff5555", font=("Consolas", 11, "bold"))
        self.status_label.pack(pady=8)

        self.last_click_label = tk.Label(self.root, text="Geçen süre: -", bg="#1a1a1a", fg="#fff", font=("Consolas", 10))
        self.last_click_label.pack(pady=3)

        # Butonlar
        button_frame = tk.Frame(self.root, bg="#1a1a1a")
        button_frame.pack(pady=15)

        btn_style = {"width": 12, "height": 2, "font": ("Segoe UI", 11, "bold"), "bd": 0, "relief": "flat", "activeforeground": "#fff", "cursor": "hand2"}

        tk.Button(button_frame, text="GÖRSEL YÜKLE", bg="#ffaa00", fg="#000", activebackground="#ff8800", command=self.add_image, **btn_style).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="BAŞLAT", bg="#00ff88", fg="#000", activebackground="#00cc70", command=self.start_bot, **btn_style).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="DURDUR", bg="#ff5555", fg="#fff", activebackground="#cc0000", command=self.stop_bot, **btn_style).grid(row=0, column=2, padx=5)

        # Alt yazı
        tk.Label(self.root, text="by Kaanth0 Software 💨", bg="#1a1a1a", fg="#666", font=("Consolas", 9)).pack(side="bottom", pady=8)

        # Timer güncelle
        self.update_timer()

    def update_timer(self):
        if self.last_click_time:
            elapsed = time.time() - self.last_click_time
            self.last_click_label.config(text=f"Geçen süre: {elapsed:.1f} saniye")
        else:
            self.last_click_label.config(text="Geçen süre: -")

        self.status_label.config(text=f"Durum: {'Aktif' if self.running else 'Kapalı'}", fg="#00ff88" if self.running else "#ff5555")
        self.root.after(100, self.update_timer)

    # Görsel ekleme
    def add_image(self):
        file_path = filedialog.askopenfilename(title="PNG Seç", filetypes=[("PNG Files", "*.png")])
        if file_path:
            dest_path = os.path.join(self.image_dir, os.path.basename(file_path))
            shutil.copy(file_path, dest_path)
            self.image_paths.append(dest_path)
            messagebox.showinfo("Başarılı", f"{os.path.basename(file_path)} yüklendi ve kullanılabilir.")

    def start_bot(self):
        if not self.running and self.image_paths:
            self.running = True
            self.bot_thread = threading.Thread(target=self.run_bot, daemon=True)
            self.bot_thread.start()

    def stop_bot(self):
        if self.running:
            self.running = False
            self.last_click_time = None  # Timer sıfırlanıyor
            if self.bot_thread and self.bot_thread.is_alive():
                self.bot_thread.join(timeout=1)

    def run_bot(self):
        first_click = True  # Başlatır başlatmaz tıklamak için
        while self.running:
            positions = []
            for path in self.image_paths:
                if os.path.exists(path):
                    pos = imagesearch(path)
                    if pos[0] != -1:
                        positions.append((pos[0] + 30, pos[1] + 80))
            if positions:
                closest = min(positions, key=lambda p: (p[0] - pyautogui.position().x)**2 + (p[1] - pyautogui.position().y)**2)
                if first_click:
                    self.safe_click(closest[0], closest[1])
                    first_click = False
                else:
                    elapsed = time.time() - self.last_click_time
                    delay = float(self.click_delay_entry.get())
                    if elapsed >= delay:
                        self.safe_click(closest[0], closest[1])
            time.sleep(0.1)

    def safe_click(self, x, y):
        try:
            self.last_click_time = time.time()
            pyautogui.moveTo(x, y)
            pyautogui.click(x, y, clicks=2, interval=0.1)
        except Exception as e:
            print(f"Tıklama hatası: {e}")

    def on_closing(self):
        self.stop_bot()
        self.root.destroy()


if __name__ == "__main__":
    Kaanth0Bot()
