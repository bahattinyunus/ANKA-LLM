# 🌿 Yeşil ANKA: Enerji Verimliliği ve Sürdürülebilir AI

Yüksek GPU gücü, yüksek enerji tüketimi demektir. Milli NPU stratejimizin kalbinde **"Performans/Watt"** oranı yatar.

## 1. Neden Enerji Verimliliği?

Türkiye'nin veri merkezlerini (HPC) kurarken enerji maliyetleri en büyük gider kalemidir. 
- NVIDIA H100: ~700W peak.
- Milli NPU Hedefi: <200W (Aynı Transformer başarımı için).

---

## 2. Yazılım Tabanlı Enerji Tasarrufu

ANKA-LLM, donanımı daha az yormak için şu teknikleri kullanır:

### A. Dynamic Activation
Modelin her katmanı her soru için çalışmaz. Basit bir Türkçe "nasılsın" sorusu için milyarlarca transistör ateşlenmez. Sadece ilgili "Expert" katmanlar aktive edilir.

### B. Precision Switching
Kritik olmayan yanıtlar 4-bit (INT4), yüksek hassasiyetli tıbbi/askeri analizler v32-bit (FP32) hassasiyetinde işlenir. Bu, anlık enerji tüketimini %60 düşürür.

---

## 3. Donanım Odaklı "Green AI" Mimari

- **In-Memory Computing:** Verinin işlemci ve bellek arasında gidip gelmesi sırasında harcanan enerjiyi sıfıra indiren "yongada bellek" tasarımı.
- **Liquid Cooling Optimization:** NPU cluster'larının ısı haritasına göre iş yükü dağıtan akıllı orkestrasyon sistemi.

---

## 🏁 Sonuç: Ekonomik ve Milli AI
Enerji verimliliği, projenin sadece çevreci değil, aynı zamanda ekonomik olarak sürdürülebilir olmasını sağlar. Daha az elektrik, daha çok zeka!
