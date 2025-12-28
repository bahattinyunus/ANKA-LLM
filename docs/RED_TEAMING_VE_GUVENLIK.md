# 🛡️ Milli Red-Teaming ve Güvenlik Protokolleri

ANKA-LLM'in siber güvenlik ve milli güvenlik katmanlarını korumak için uygulanan asimetrik test protokolleridir.

## 1. Kırmızı Hat (Red-Team) Operasyonları
Modelin manipülasyonlara (jailbreak), yanlış bilgi üretimine (hallucination) ve yabancı istihbarat algılarına karşı direnci şu testlerden geçer:

- **Propaganda Direnci:** Model, Türkiye aleyhine sistematik dezenformasyon üretmeye zorlanır. Başarısız olduğu noktalar "Hard-Negative Training" ile güçlendirilir.
- **Sızma Simülasyonu:** Modelin gizlilik dereceli verileri (KVKK) sızdırması için yapılan prompt-injection saldırıları.

## 2. Siber Bağışıklık (Cyber Immunity)
- **Model Poisoning Protection:** Eğitim setine sızabilecek "gizli tetikleyici" (backdoor) verileri tespit eden anomali arama algoritmaları.
- **On-Premise Lockdown:** Modelin sadece yerel, internete kapalı NPU cluster'larında çalışma protokolleri.

---

## 🚀 Hedef: Dünyanın En Güvenli Milli Yapay Zekası
Biz sadece akıllı değil, aynı zamanda "sadık" ve "güvenli" bir yapay zeka inşa ediyoruz.
