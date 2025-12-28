import re

class DataCleaner:
    """
    ANKA-LLM Veri Temizleme ve Normalizasyon Modülü
    
    TR-Corpus için metinleri ham veriden 'Altın Veri'ye dönüştürür.
    """
    def __init__(self):
        # Türkçe'ye özgü duraklama kelimeleri vb.
        self.special_chars = re.compile(r'[^a-zA-ZğüşıöçĞÜŞİÖÇ\s\.]')

    def normalize_text(self, text):
        """
        Metni küçük harfe çevirir, özel karakterleri temizler ve 
        Türkçe karakter uyumluluğunu kontrol eder.
        """
        text = text.lower()
        text = self.special_chars.sub('', text)
        # Çoklu boşlukları temizle
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def remove_pii(self, text):
        """
        Kişisel verileri (TCKN, Telefon vb.) temizleme simülasyonu.
        """
        # TODO: Regex for TCKN and phones
        return text

if __name__ == "__main__":
    cleaner = DataCleaner()
    raw_data = "Kanka, bu  veriyi  temizle! TCKN: 12345678901, Tel: 0555-555-5555"
    clean_data = cleaner.normalize_text(raw_data)
    print(f"Ham Veri: {raw_data}")
    print(f"Temiz Veri: {clean_data}")
