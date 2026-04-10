def caesar_sifrele(metin, kaydirma):
    sonuc = []
    for h in metin:
        if h.isalpha():
            # Büyük harf için 65 (A), küçük harf için 97 (a)
            offset = 65 if h.isupper() else 97
            # Karakteri kaydır ve listeye ekle
            yeni_harf = chr((ord(h) - offset + kaydirma) % 26 + offset)
            sonuc.append(yeni_harf)
        else:
            # Harf değilse (boşluk, !, ? vs.) direkt ekle
            sonuc.append(h)
    return "".join(sonuc)

def caesar_coz(metin, kaydirma):
    # Şifreleme fonksiyonunu ters kaydırma ile çağırıyoruz
    return caesar_sifrele(metin, -kaydirma)