import tkinter as tk
from tkinter import messagebox

# Modül isimlerinizin doğru olduğunu ve fonksiyonların bu isimlerle dışa aktarıldığını varsayıyorum.
from caesar import *
from vigenere import *
from hybrid import *
from attack import *

# =========================
# FONKSİYONLAR
# =========================

def encrypt_action():
    text = entry_text.get().strip()
    key = entry_key.get().strip()
    method = method_var.get()

    if not text:
        messagebox.showwarning("Uyarı", "Lütfen şifrelenecek metni girin.")
        return

    try:
        if method == "Caesar":
            if not key.isdigit():
                messagebox.showerror("Hata", "Caesar için anahtar sayı olmalıdır!")
                return
            result = caesar_sifrele(text, int(key))

        elif method == "Vigenere":
            if not key.isalpha():
                messagebox.showerror("Hata", "Vigenere için anahtar sadece harf olmalıdır!")
                return
            result = vigenere_sifrele(text, key)

        else: # Hybrid
            if not key:
                messagebox.showerror("Hata", "Hybrid yöntem için anahtar gereklidir!")
                return
            result = hybrid_encrypt(text, key)

        output.delete("1.0", tk.END)
        output.insert(tk.END,
            f"--- ŞİFRELEME SONUCU ---\n"
            f"Yöntem: {method}\n"
            f"Orijinal Metin: {text}\n"
            f"Anahtar: {key}\n"
            f"------------------------\n"
            f"Şifreli Metin: {result}\n"
        )
    except Exception as e:
        messagebox.showerror("Hata", f"İşlem sırasında hata oluştu: {str(e)}")


def decrypt_action():
    text = entry_text.get().strip()
    key = entry_key.get().strip()
    method = method_var.get()

    if not text:
        messagebox.showwarning("Uyarı", "Lütfen çözülecek metni girin.")
        return

    try:
        if method == "Caesar":
            if not key.isdigit():
                messagebox.showerror("Hata", "Caesar için anahtar sayı olmalıdır!")
                return
            result = caesar_coz(text, int(key))

        elif method == "Vigenere":
            if not key.isalpha():
                messagebox.showerror("Hata", "Vigenere için anahtar sadece harf olmalıdır!")
                return
            result = vigenere_coz(text, key)

        else: # Hybrid
            if not key:
                messagebox.showerror("Hata", "Hybrid yöntem için anahtar gereklidir!")
                return
            result = hybrid_decrypt(text, key)

        output.delete("1.0", tk.END)
        output.insert(tk.END,
            f"--- ŞİFRE ÇÖZME SONUCU ---\n"
            f"Yöntem: {method}\n"
            f"Şifreli Metin: {text}\n"
            f"Anahtar: {key}\n"
            f"------------------------\n"
            f"Çözülmüş Metin: {result}\n"
        )
    except Exception as e:
        messagebox.showerror("Hata", f"İşlem sırasında hata oluştu: {str(e)}")


def analiz_action():
    text = entry_text.get().strip()
    if not text:
        messagebox.showwarning("Uyarı", "Analiz için metin girin.")
        return

    freq = harf_frekansi(text)
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"--- FREKANS ANALİZİ ---\nMetin: {text[:30]}...\n\n")
    
    # Harfleri alfabetik veya değere göre sıralayarak yazdırmak daha okunaklı olur
    for k, v in sorted(freq.items()):
        output.insert(tk.END, f"'{k}': {v}\n")


def attack_action():
    text = entry_text.get().strip()
    key = entry_key.get().strip()
    method = method_var.get()

    if not text:
        messagebox.showwarning("Uyarı", "Saldırı için metin girin.")
        return

    output.delete("1.0", tk.END)
    output.insert(tk.END, f"--- SALDIRI (ATTACK) SONUÇLARI ---\nYöntem: {method}\n\n")

    if method == "Caesar":
        # Tüm anahtar olasılıklarını dene (0-25 arası)
        for i in range(1, 26):
            try:
                output.insert(tk.END, f"Anahtar {i:02}: {caesar_coz(text, i)}\n")
            except: continue

    elif method == "Vigenere":
        if key:
            output.insert(tk.END, f"Anahtar '{key}' ile deneme:\n{vigenere_coz(text, key)}")
        else:
            output.insert(tk.END, "Vigenere atağı için (sözlük/brute-force) anahtar veya aday kelime girmelisiniz.")

    else:
        if key:
            output.insert(tk.END, f"Anahtar '{key}' ile deneme:\n{hybrid_decrypt(text, key)}")
        else:
            output.insert(tk.END, "Hybrid atak için anahtar bilgisi gerekli.")

# =========================
# GUI
# =========================

root = tk.Tk()
root.title("KriptoYC Projesi")
root.geometry("600x700")
root.configure(padx=20, pady=20)

method_var = tk.StringVar(value="Caesar")

# Arayüz Elemanları
tk.Label(root, text="Şifreleme Yöntemi", font=("Arial", 10, "bold")).pack(pady=(0,5))
frame_radio = tk.Frame(root)
frame_radio.pack()
tk.Radiobutton(frame_radio, text="Caesar", variable=method_var, value="Caesar").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_radio, text="Vigenere", variable=method_var, value="Vigenere").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_radio, text="Hybrid", variable=method_var, value="Hybrid").pack(side=tk.LEFT, padx=10)

tk.Label(root, text="İşlenecek Metin:", font=("Arial", 9)).pack(pady=(15,0), anchor="w")
entry_text = tk.Entry(root, width=70)
entry_text.pack(pady=5)

tk.Label(root, text="Anahtar (Key):", font=("Arial", 9)).pack(pady=(5,0), anchor="w")
entry_key = tk.Entry(root, width=70)
entry_key.pack(pady=5)

# Butonlar
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=15)

tk.Button(frame_buttons, text="Şifrele", width=12, bg="#d4edda", command=encrypt_action).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Şifre Çöz", width=12, bg="#f8d7da", command=decrypt_action).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Frekans Analizi", width=12, command=analiz_action).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Atak Yap", width=12, bg="#fff3cd", command=attack_action).grid(row=0, column=3, padx=5)

tk.Label(root, text="Çıktı Ekranı:", font=("Arial", 9, "italic")).pack(anchor="w")
output = tk.Text(root, height=20, width=70, font=("Courier New", 10))
output.pack(pady=5)

root.mainloop()