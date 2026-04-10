import string

def harf_frekansi(metin):
    # Sadece harfleri filtrele ve büyük harfe çevir
    temiz_metin = "".join(filter(str.isalpha, metin.upper()))
    toplam_harf = len(temiz_metin)
    
    # Başlangıç sözlüğü
    freq = {c: 0 for c in string.ascii_uppercase}
    
    for h in temiz_metin:
        if h in freq:
            freq[h] += 1
            
    # Eğer toplam harf 0 değilse yüzdelik oranları da hesaplayabiliriz (Opsiyonel)
    # Sonuçları daha anlamlı kılmak için sadece 0'dan büyük olanları döndürelim:
    return {k: v for k, v in freq.items() if v > 0}