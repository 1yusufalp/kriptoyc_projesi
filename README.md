# 🔐 KriptoYC Projesi

Bu proje, klasik şifreleme algoritmalarını ve basit kriptanaliz tekniklerini bir araya getiren kapsamlı bir **kriptografi uygulamasıdır**. Eğitim amaçlı geliştirilmiş olup, hem şifreleme yöntemlerini anlamayı hem de bu yöntemlere karşı analiz yapmayı hedefler.

---

## 📌 Proje Amacı

Bu projenin amacı:

* Temel kriptografi algoritmalarını uygulamak
* Şifreleme ve deşifreleme süreçlerini göstermek
* Basit saldırı (attack) tekniklerini öğretmek
* Kullanıcıya deneysel bir analiz ortamı sunmaktır

---

## ⚙️ Özellikler

### 🔡 1. Caesar Cipher

* Harfleri belirli bir kaydırma (shift) ile değiştirir
* Basit ve klasik bir şifreleme yöntemidir
* Şifreleme ve çözme (decrypt) desteği vardır

---

### 🔤 2. Vigenère Cipher

* Anahtar kelime kullanarak daha güçlü şifreleme sağlar
* Caesar şifresinin geliştirilmiş halidir
* Çoklu kaydırma mantığı ile çalışır

---

### 🔐 3. Hibrit Şifreleme Sistemi

Bu projeye özel geliştirilmiş çok katmanlı sistemdir:

* ✔️ Anahtar tabanlı alfabe dönüşümü
* ✔️ Blok bazlı ters çevirme işlemi
* ✔️ Rastgele karakter ekleme (gürültü)

Bu sayede:

* Metin hem yapısal hem içerik olarak karmaşık hale gelir

---

### 🧠 4. Analiz ve Attack Paneli

* Şifreli metinler üzerinde analiz yapılabilir
* Frekans analizi gibi teknikler uygulanabilir
* Olası anahtar tahminleri yapılabilir
* Zayıf şifreleme yöntemleri test edilebilir

---

## 🛠️ Kurulum

Projeyi çalıştırmak için:

```bash
git clone <repo_link>
cd kriptosistem-projesi
python main.py
```

Gereksinimler:

* Python 3.x

(Opsiyonel kütüphaneler varsa buraya eklenebilir)

---

## ▶️ Kullanım

Program çalıştırıldığında kullanıcıya bir menü sunulur:

* Şifreleme işlemleri
* Deşifre işlemleri
* Analiz araçları

Kullanıcı:

1. Algoritmayı seçer
2. Metni girer
3. Gerekirse anahtar belirler
4. Sonucu görüntüler

---

## 📂 Proje Yapısı

```bash
.
├── main.py              # Ana uygulama
├── caesar.py            # Caesar cipher işlemleri
├── vigenere.py          # Vigenere cipher işlemleri
├── hybrid.py            # Hibrit şifreleme sistemi
├── analysis.py          # Analiz ve saldırı araçları
└── README.md            # Proje dokümantasyonu
```

---

## 🔍 Örnek Kullanım

**Girdi:**

```
Metin: HELLO WORLD
Anahtar: KEY
```

**Çıktı:**

```
Şifreli metin: XJH...
```

(Algoritmaya göre değişir)

---

## ⚠️ Güvenlik Notu

Bu projede kullanılan algoritmalar:

* Eğitim amaçlıdır
* Modern güvenlik standartlarına uygun değildir

Gerçek uygulamalarda:

* AES, RSA gibi güçlü algoritmalar kullanılmalıdır

---

## 🚀 Geliştirme Fikirleri

* GUI (arayüz) ekleme
* Dosya şifreleme desteği
* Daha gelişmiş kriptanaliz araçları
* Modern algoritmaların entegrasyonu

---

## 👨‍💻 Katkı

Katkıda bulunmak için:

1. Fork oluştur
2. Yeni bir branch aç
3. Değişiklik yap
4. Pull request gönder

---

## 📄 Lisans

Bu proje eğitim amaçlıdır ve açık kaynak olarak paylaşılabilir.

---

## ✨ Sonuç

Bu proje sayesinde:

* Kriptografinin temellerini öğrenebilir
* Farklı şifreleme tekniklerini karşılaştırabilir
* Basit saldırı yöntemlerini deneyimleyebilirsin

---
