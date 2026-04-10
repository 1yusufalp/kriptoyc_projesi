def vigenere_islem(metin, anahtar, mod="sifrele"):
    sonuc = []
    anahtar = anahtar.upper()
    j = 0
    
    # Şifreleme için +1, çözme için -1 çarpanı
    yon = 1 if mod == "sifrele" else -1

    for h in metin:
        if h.isalpha():
            offset = 65 if h.isupper() else 97
            kaydir = (ord(anahtar[j % len(anahtar)]) - 65) * yon
            
            yeni_harf = chr((ord(h) - offset + kaydir) % 26 + offset)
            sonuc.append(yeni_harf)
            j += 1
        else:
            sonuc.append(h)
            
    return "".join(sonuc)

def vigenere_sifrele(metin, anahtar):
    return vigenere_islem(metin, anahtar, "sifrele")

def vigenere_coz(metin, anahtar):
    return vigenere_islem(metin, anahtar, "coz")