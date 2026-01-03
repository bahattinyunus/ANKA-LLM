# 📊 TR-Corpus v1: Milli Veri Madenciliği Mimarisi

Anka Silicon Dynamics'in zekası, beslendiği verinin kalitesiyle sınırlıdır. Bu doküman, Türkiye'nin "Altın Veri Seti"ni oluşturma stratejisini detaylandırır.

## 1. Veri Kaynakları: Katmanlı Mimari

| Katman | Kaynak Türü | Hedef | Hacim (Tahmini) |
| --- | --- | --- | --- |
| **L1: Akademik** | DergiPark, Tez Arşivleri | Teknik ve bilimsel muhakeme. | 50B+ Token |
| **L2: Hukuki** | Mevzuat, Yargıtay Kararları | Mantıksal çıkarım ve resmi dil. | 20B+ Token |
| **L3: Tarihsel** | Dijital Osmanlı Arşivleri, TDK | Kültürel süreklilik ve dil derinliği. | 10B+ Token |
| **L4: Güncel** | Yerel Haberler, Kurumsal Raporlar | Güncel dünya bilgisi. | 100B+ Token |

---

## 2. Sentetik Veri Rafinerisi (Synthetic Refiner)

Gerçek verinin yetmediği veya gizlilik içerdiği durumlarda, Anka Silicon Dynamics kendi verisini üretir:

1.  **Logical Injection:** Matematik ve mantık problemlerinin Türkçe kurgulanması.
2.  **OCR Pipeline:** El yazması eserlerin ve eski gazete arşivlerinin "LLM-Ready" metne dönüştürülmesi.
3.  **De-biasing:** Verideki yabancı kültür etkilerinin ve dezenformasyonun temizlenmesi.

---

## 3. Veri Güvenliği ve Egemenliği

- **Air-gapped Processing:** Kritik veriler internet bağlantısı olmayan izole NPU cluster'larında işlenir.
- **Anonymization:** Şahıs ve kurum verileri, Moore-Anonymization algoritmalarıyla temizlenir.

---

## 🚀 Hedef: 500 Milyar Yüksek Kaliteli Türkçe Token
Bu veri seti, sadece Anka Silicon Dynamics için değil, Türkiye'nin gelecekteki tüm yapay zeka projeleri için bir "Milli Dijital Hafıza" olacaktır.
