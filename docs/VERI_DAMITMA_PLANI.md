# 🧪 Veri Damıtma ve Sentetik Veri Rafinerisi

Bu doküman, milyar dolarlık donanım parkurlarına sahip olmadan, dünya standartlarında bir Türkçe LLM eğitmenin en gerçekçi yolu olan **"Knowledge Distillation" (Bilgi Damıtma)** tekniklerini içerir.

## 1. Neden Damıtma (Distillation)?

Eğer elinizde 20.000 adet H100 yoksa, modeli sıfırdan eğitmek (Pre-training) yerine, mevcut dev modellerin **mantık silsilesini (reasoning)** küçük bir modele öğretmelisiniz.

* **Maliyet:** Sıfırdan eğitim $100M+ iken, damıtma yöntemiyle ince ayar (Fine-tuning) $10k - $50k arasıdır.
* **Verimlilik:** Dev modellerin içindeki "gürültü" (noise) atılır, sadece "öz zeka" (signal) alınır.

---

## 2. Uygulama Stratejisi: "Teacher-Student" Modeli

### A. Öğretmen (Teacher) Seçimi

En yüksek muhakeme yeteneğine sahip modeller "Öğretmen" olarak kullanılır.
* *Seçenekler:* GPT-4o, Claude 3.5 Sonnet, Llama-3-70B.

### B. Öğrenci (Student) Seçimi

Türkiye’deki mevcut GPU altyapısında (Örn: 8x A100/H100) rahatça eğitilebilecek ve son kullanıcıda (laptop/telefon) çalışabilecek modeller.
* *Seçenekler:* Llama-3-8B, Mistral-7B, Phi-3-Mini.

---

## 3. Adım Adım Veri Damıtma Boru Hattı (Pipeline)

### 1. Adım: Soru Havuzu Oluşturma (Seed Tasks)

Türkiye'ye özgü 10.000 temel görev belirlenir.
* *Örnek:* "Türk Borçlar Kanunu'na göre temerrüt şartlarını açıkla."
* *Örnek:* "Anadolu Selçuklu Devleti'nin yıkılış sürecini sosyo-ekonomik açıdan analiz et."

### 2. Adım: CoT (Chain of Thought) Üretimi

Öğretmen modele bu sorular sorulur ama sadece cevap istenmez. **Düşünme aşamalarını** (step-by-step reasoning) açıklaması istenir.

### 3. Adım: Kalite Kontrol (Refining)

Üretilen cevaplar, küçük bir yerli uzman grubu veya daha üst bir model tarafından "Kültürel Uygunluk" ve "Doğruluk" testinden geçirilir. Yanlış bilgi (hallucination) temizlenir.

### 4. Adım: SFT (Supervised Fine-Tuning)

Elde edilen bu "Yüksek Kaliteli Türkçe Mantık Seti", Öğrenci modelimize (ANKA-7B) öğretilir. Model artık bir Amerikalı gibi değil, bir Türk uzman gibi düşünmeye başlar.

---

## 🛠️ Kullanılacak Teknik Araç Seti (Stack)

* **Eğitim Kütüphanesi:** [Unsloth](https://github.com/unslothai/unsloth) (Bellek kullanımını %80 azaltır, eğitimi 2 kat hızlandırır).
* **Veri Üretim Araçları:** [Distilabel](https://github.com/argilla-io/distilabel) (Karmaşık damıtma iş akışlarını otomatikleştirir).

---

## 📈 Beklenen Sonuç: "Mistral-TR" Moment

Bu aşamanın sonunda elimizde;
1. Google Gemini kadar büyük olmayan ama,
2. **Türkiye özelindeki sorularda** Google'dan daha doğru, daha hızlı ve daha ucuz cevap veren bir model kalacaktır.

---

## 🚩 Kritik Uyarı: KVKK ve Veri Gizliliği

Damıtma işlemi sırasında kamuya açık olmayan, gizlilik dereceli veriler asla ticari API'lere (OpenAI vb.) gönderilmemelidir. Bu tür veriler için içeride koşturulan **Llama-3-70B** gibi açık kaynaklı "Yerel Öğretmenler" kullanılmalıdır.
