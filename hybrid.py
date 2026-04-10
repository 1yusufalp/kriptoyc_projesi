import random
import string

ALPHABET = string.ascii_uppercase

def yeni_alfabe_olustur(anahtar):
    anahtar = "".join(dict.fromkeys(anahtar.upper()))
    # Sadece alfabede olan karakterleri filtrele
    anahtar = "".join([c for c in anahtar if c in ALPHABET])
    kalan = "".join([c for c in ALPHABET if c not in anahtar])
    return anahtar + kalan

def asama1_sifrele(metin, anahtar):
    yeni = yeni_alfabe_olustur(anahtar)
    # Metni büyütüp sadece alfabedeki harfleri işleme sokalım
    return "".join(yeni[ALPHABET.index(c)] if c in ALPHABET else c for c in metin.upper())

def asama1_coz(metin, anahtar):
    yeni = yeni_alfabe_olustur(anahtar)
    return "".join(ALPHABET[yeni.index(c)] if c in yeni else c for c in metin.upper())

def blok_islem(metin, boyut=3):
    # Hem şifreleme hem çözme için aynı ters çevirme mantığı kullanılır
    sonuc = ""
    for i in range(0, len(metin), boyut):
        blok = metin[i:i+boyut]
        sonuc += blok[::-1]
    return sonuc

def asama3_sifrele(metin):
    sonuc = ""
    # Her 2 karakterde bir 1 rastgele karakter ekle
    for i in range(0, len(metin), 2):
        parca = metin[i:i+2]
        sonuc += parca
        if len(parca) == 2: # Sona gelmediysek ekle
            sonuc += random.choice(ALPHABET)
    return sonuc

def asama3_coz(metin):
    # Her 3. karakteri (eklenen rastgele harfi) atla
    return "".join(metin[i] for i in range(len(metin)) if (i+1) % 3 != 0)

def hybrid_encrypt(metin, anahtar):
    # 1. Yer Değiştirme -> 2. Blok Tersleme -> 3. Gürültü Ekleme
    s1 = asama1_sifrele(metin, anahtar)
    s2 = blok_islem(s1)
    return asama3_sifrele(s2)

def hybrid_decrypt(metin, anahtar):
    # Ters sıra: 1. Gürültü Sil -> 2. Blok Tersleme -> 3. Yer Değiştirme Çöz
    c1 = asama3_coz(metin)
    c2 = blok_islem(c1)
    return asama1_coz(c2, anahtar)