# 📊 ANKA-LLM: Değerlendirme Metrikleri ve Başarım Ölçütleri

Bir modelin "Milli" ve "Üstün" olması sadece matematiksel bir iddia değil, ölçülebilir bir gerçeklik olmalıdır. ANKA-LLM, başarısını şu metriklerle kanıtlar:

## 1. Standart LLM Benchmark'ları (Türkçe Adaptasyonu)

- **MMLU-TR:** Muazzam Çok Görevli Dil Anlama testinin Türkçe'ye en rafine şekilde çevrilmiş ve yerelleştirilmiş versiyonu.
- **TR-HellaSwag:** Sağduyulu muhakeme yeteneğinin Türkçe atasözleri ve deyimler üzerinden testi.
- **GSM8K-TR:** İlkokul seviyesindeki matematik problemlerinin Türkçe mantık silsilesiyle çözümü.

---

## 2. Asimetrik Üstünlük Metrikleri (Özgün)

- **Morfolojik Verimlilik (Token Ratio):** Aynı metni NVIDIA/OpenAI modellerinden kaç kat daha az token ile temsil edebiliyoruz? (Hedef: %30 Tasarruf).
- **Kültürel Uyumluluk Skoru (C-Eval TR):** Modelin Türk tarih, hukuk ve etik değerlerine verdiği yanıtların doğruluğu.
- **Düşük Kaynaklı Başarım (Zero-Shot TR):** Klasik modellerin anlamadığı nadir Türkçe lehçeleri ve teknik terminolojideki anlama kapasitesi.

---

## 3. Donanım Bağımsızlığı Metrikleri

- **Performans/NPU-Area:** Yerli çipteki kapladığı alan başına ürettiği saniye/token hızı.
- **Energy-to-Intelligence:** Bir yanıt üretmek için harcanan Joule miktarı.

---

## 🚀 Hedef: "Kağıt Üstünde Değil, Sahada Üstünlük"
Biz sadece skor peşinde değiliz; ANKA-LLM'in bir Türk mühendisine, hukukçusuna veya askerine sağladığı gerçek zamanlı değerle ölçülüyoruz.
