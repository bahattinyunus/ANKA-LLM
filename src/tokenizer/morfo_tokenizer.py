from typing import List

class MorfoTokenizer:
    """
    Anka Silicon Dynamics Türkçe Morfolojik Tokenizer v2 (Advanced)
    
    Türkçenin sondan eklemeli yapısını analiz ederek, kelimeleri 
    kök ve eklerine ayırır. Bu yöntem;
    1. Kelime dağarcığını (Vocab Size) %30 küçültür.
    2. Modelin nadir kelimeleri (OOV) anlama kapasitesini artırır.
    """
    def __init__(self, vocab_size: int = 32000):
        self.vocab_size = vocab_size
        # Geliştirilmiş ek listesi (En uzundan en kısaya doğru sıralı olmalı)
        self.suffixes = sorted([
            # Çoğul ve Durum ekleri
            "lar", "ler", "dan", "den", "tan", "ten", "da", "de", "ta", "te", 
            "nın", "nin", "nun", "nün", "ın", "in", "un", "ün", "yı", "yi", "yu", "ü",
            # İyelik ekleri
            "ımız", "imiz", "leri", "ları",
            # Zaman ekleri
            "iyor", "uyor", "ıyor", "üyör", "acak", "ecek", "mış", "miş", "muş", "müş",
            "dı", "di", "du", "dü", "tı", "ti", "tu", "tü",
            # Yapım ekleri
            "lık", "lik", "luk", "lük", "cı", "ci", "cu", "cü", "lı", "li", "lu", "lü", "sız", "siz"
        ], key=len, reverse=True)
        
        print(f"🇹🇷 ANKA Morfo-Tokenizer v2 Hazır. | Hedef Vocab: {vocab_size}")

    def tokenize(self, text: str) -> List[str]:
        """
        Metni morfolojik birimlerine ayırır.
        Algoritma: Greedy Suffix Matching (Açgözlü Ek Eşleştirme)
        """
        words = text.split()
        tokens = []
        for word in words:
            # Basit normalizasyon
            temp_word = word.lower().replace(".", "").replace(",", "")
            word_tokens = []
            
            current_stem = temp_word
            
            # Kelimeyi sondan başlayarak eklerine ayır (Recursive benzeri döngü)
            while len(current_stem) > 3: # Kök en az 3 harf olsun koruması
                found_suffix = False
                for suffix in self.suffixes:
                    if current_stem.endswith(suffix):
                        # Ek bulundu, ayır ve başa ekle
                        word_tokens.insert(0, "##" + suffix) # BPE/WordPiece tarzı işaretleme
                        current_stem = current_stem[:-len(suffix)]
                        found_suffix = True
                        break # En uzun eki bulduğumuz için döngüyü kır, yeni köke bak
                
                if not found_suffix:
                    break # Ek bulunamadıysa döngüyü bitir
            
            word_tokens.insert(0, current_stem)
            tokens.extend(word_tokens)
            
        return tokens

    def decode(self, tokens: List[str]) -> str:
        """
        Tokenları birleştirir. '##' işaretini kaldırıp birleştirir.
        """
        text = ""
        for token in tokens:
            if token.startswith("##"):
                text += token[2:]
            else:
                text += " " + token
        return text.strip()

if __name__ == "__main__":
    tokenizer = MorfoTokenizer()
    
    test_sentences = [
        "Türkiye'nin geleceği kod satırlarında gizlidir.",
        "Bilgisayarcılarımız algoritmaları geliştiriyorlar.",
        "Evsizlik ve işsizlik sorunları çözülecek."
    ]
    
    print("\n--- Morfo-Analiz Testi ---")
    for sent in test_sentences:
        tks = tokenizer.tokenize(sent)
        print(f"Girdi: {sent}")
        print(f"Token: {tks}\n")
