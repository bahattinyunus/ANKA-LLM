# 🛰️ Milli NPU (Yapay Zeka İşlemcisi) Yazılım ve Mimari Gereksinimleri

**Vizyon:** Türkiye’nin ilk yerli yapay zeka hızlandırıcısının, sadece bir donanım olarak değil, ANKA-LLM ekosistemiyle %100 uyumlu bir "akıllı çekirdek" olarak tasarlanması.

## 1. Mimari Odak: Verimlilik > Genel Amaç

NVIDIA, GPU'larını her şeyi (video kurgu, oyun, madencilik) yapabilecek şekilde tasarlar. Milli NPU, sadece **Transformer** mimarilerini (LLM'lerin kalbi) en hızlı koşturacak şekilde optimize edilmelidir.

* **Matris Çarpım Birimleri (Tensor Cores):** NPU'nun %80'i matris çarpımı yapan çekirdeklerden oluşmalı.
* **SRAM Yakınlığı:** Veri transferi (HBM) darboğazını aşmak için, model ağırlıklarının işlemciye en yakın olduğu "Near-Memory Computing" mimarisi tercih edilmeli.

---

## 2. Yazılım Katmanı (Software Stack) Gereksinimleri

Donanım ne kadar iyi olursa olsun, yazılım kütüphanesi yoksa ölü bir yatırımdır.

### A. CUDA'ya Yerli Alternatif: ANKA-Compute

* **Kernel Seviyesi:** C++ ve Triton tabanlı, düşük seviyeli bir kütüphane geliştirilmeli.
* **Pytorch/Tensorflow Desteği:** Yerli NPU, global kütüphanelerle "Plug-and-Play" çalışmalı. Mühendisler kodlarını değiştirip `device="npu"` yazdığında sistem ayağa kalkmalı.

### B. Morfolojik Hızlandırma Katmanı

Türkçe gibi sondan eklemeli dillerde tokenizasyon maliyetlidir.

* **Donanım Seviyesi Tokenizer:** Tokenization işlemini CPU yerine NPU içinde, donanım seviyesinde yapan özel bir devre bloğu (Logic Gate) eklenmelidir.

---

## 3. Sayısal Hassasiyet ve Sıkıştırma (Precision)

Modern LLM'ler artık 32-bit veya 16-bit çalışmıyor.

* **Native FP8 ve INT4 Desteği:** NPU, model ağırlıklarını 4-bit seviyesinde (Quantized) doğal olarak işlemeli. Bu, işlem hızını 4 kat artırırken enerji tüketimini 10 kat düşürür.
* **Sparsity (Seyreklik) Desteği:** Yapay zeka matrislerindeki "0" (boş) değerleri atlayan ve sadece anlamlı veriyi işleyen bir donanım mimarisi.

---

## 4. Ölçeklenebilirlik: Interconnect (Yongalar Arası Bağlantı)

Tek bir çip Gemini'yi eğitemez. Binlerce çip birbiriyle konuşmalıdır.

* **Milli Link:** NVIDIA'nın NVLink teknolojisine muadil, işlemciler arası 400 GB/s ve üzeri veri transferi sağlayan yerli bir protokol geliştirilmelidir.

---

## 5. Uygulama Senaryoları (Referans Tasarımlar)

| Tip | Hedef Cihaz | Kullanım Amacı |
| --- | --- | --- |
| **ANKA-Nano** | İHA / SİHA / Akıllı Telefon | Çevrimdışı, yerinde (Edge) hızlı analiz. |
| **ANKA-Pro** | Yerel Sunucu / Hastane / Adliye | KVKK uyumlu, internete kapalı kurum içi LLM. |
| **ANKA-Süper** | Veri Merkezi (HPC) | Milyarlarca parametreli model eğitimi. |

---

## 🚩 Kritik Strateji: "Software-First Hardware"

Bizim donanım mühendislerimiz, çipi tasarlamaya başlamadan önce bu repodaki **ANKA-LLM Python kodlarını** simülatörlerde çalıştırmalıdır. Çip, yazılıma uymalı; yazılım çipe uydurulmaya çalışılmamalıdır.
