import time
import random

class NPUInferenceEngine:
    """
    ANKA-LLM Milli NPU Çıkarım (Inference) Simülatörü
    
    Yerli NPU mimarisinin standart GPU'lara göre asimetrik 
    üstünlüğünü (Perf/Watt ve Gecikme) simüle eder.
    """
    def __init__(self, chip_type="ANKA-Pro"):
        self.chip_type = chip_type
        print(f"--- {chip_type} Inference Engine Active ---")

    def run_inference(self, prompt, model_size="8B"):
        print(f"Sorgu İşleniyor: '{prompt}'")
        
        # GPU Simülasyonu
        gpu_time = random.uniform(2.5, 4.0)
        gpu_watt = 350
        
        # NPU Simülasyonu (Asimetrik Üstünlük)
        npu_time = random.uniform(0.5, 0.8)
        npu_watt = 45 # FP8/INT4 verimliliği
        
        print("\n[PERFORMANS KARŞILAŞTIRMASI]")
        print(f"Standart GPU: {gpu_time:.2f}s | {gpu_watt}W")
        print(f"ANKA NPU    : {npu_time:.2f}s | {npu_watt}W [ASİMETRİK KAZANÇ]")
        
        gain = (gpu_time / npu_time)
        print(f"\nSonuç: ANKA NPU, bu görevde {gain:.1f}x daha hızlıdır.")

if __name__ == "__main__":
    engine = NPUInferenceEngine()
    engine.run_inference("Türkiye'nin 2030 dijital stratejisi nedir?")
