@echo off
echo ==================================================
echo         ANKA-LLM OTOMASYON MERKEZI v1.0
echo ==================================================
echo.
echo 1. Eğitim Simülasyonunu Çalıştır
echo 2. Tokenizer'ı Test Et
echo 3. Veri Temizleme Aracını Başlat
echo 4. Çıkış
echo.
set /p choice="Seçiminizi yapın (1-4): "

if "%choice%"=="1" (
    python src\simulation\training_sim.py
    pause
    goto :eof
)
if "%choice%"=="2" (
    python src\tokenizer\morfo_tokenizer.py
    pause
    goto :eof
)
if "%choice%"=="3" (
    python scripts\data_cleaner.py
    pause
    goto :eof
)
if "%choice%"=="4" (
    exit
)

echo Geçersiz seçim.
pause
