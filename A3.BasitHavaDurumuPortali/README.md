#*********************************************************
#* TechIstanbulPython2025 kursu bitirme projesi         **
#* Akıllı Ev Girişi Hava Durumu Ekranı                  **
#* Timur Çakal 10.11.2025 v2.23                         **
#* https://www.linkedin.com/in/Timur67/                 **
#*********************************************************
# Akıllı Ev Girişi Hava Durumu Ekranı

Bu proje, MSN Hava Durumu web sitesinden alınan verileri işleyerek, ev girişine yerleştirilen Android tablette sürekli güncel hava durumu bilgilerini gösteren bir uygulamadır.

## Özellikler

- MSN Hava Durumu web sitesinden otomatik ekran görüntüsü alma
- Belirli bir bölgenin hava durumu bilgilerini görüntüleme
- Otomatik çerez kabulü ile kullanıcı etkileşimi gerektirmeden çalışma
- Görüntüleri T100 tablete uygun şekilde işleme ve gönderme
- Ev girişindeki ziyaretçiler için anlık hava durumu bilgisi sunma
- Tam otomatik çalışma, manuel müdahale gerektirmeden sürekli güncelleme

## Gereksinimler

### Temel Gereksinimler
- Python 3.7 veya üzeri
- İnternet bağlantısı (hava durumu verileri için)

### Python Kütüphaneleri
Aşağıdaki kütüphaneler kurulu olmalıdır:
```bash
pip install selenium pillow webdriver-manager
```

### T100 Tablet Özellikleri
- İşletim Sistemi: Windows 10/11
- Ekran Çözünürlüğü: 1024x600 piksel

## Kurulum
### Windows Bilgisayarlar İçin:

1. Python'u yükleyin (henüz yüklü değilse):
   - [Python resmi sitesinden](https://www.python.org/downloads/) indirin
   - Kurulum sırasında "Add Python to PATH" seçeneğini işaretlemeyi unutmayın

2. Kodu indirin:
   ```bash
   git clone https://github.com/yesilege/TechIstanbulPython2025.git
   cd TechIstanbulPython2025/Tim'sWeatherTerminal
   ```
   
   Veya manuel olarak indirip çıkarın. Eğer klasör adı '1' ise şu şekilde güncelleyin:
   ```bash
   ren "1" "Tim'sWeatherTerminal"
   cd "Tim'sWeatherTerminal"
   ```

3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. Programı çalıştırın:
   ```bash
   python ders04screenshot.py
   ```

### T100 Tablet İçin Özel Kurulum:

1. T100 tablette oturum açın
2. Yukarıdaki Windows kurulum adımlarını takip edin
3. Başlangıç klasörüne kısayol ekleyin (isteğe bağlı):
   - `ders04screenshot.py` dosyasına sağ tıklayın
   - "Kısayol oluştur" seçeneğini seçin
   - Kısayolu kesip `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` klasörüne yapıştırın

### Yapılandırma (İsteğe Bağlı)

Farklı bir konum için hava durumu göstermek isterseniz, `ders04screenshot.py` dosyasında aşağıdaki satırı değiştirin:

```python
driver.get("https://www.msn.com/tr-tr/havadurumu/havadurumutahmini/in-Eregli,Zonguldak")
```

URL'deki `Eregli,Zonguldak` kısmını istediğiniz şehir bilgisiyle değiştirebilirsiniz.

## Kullanım

1. Program T100 tablette çalıştırıldığında otomatik olarak:
   - Tarayıcı açılır
   - MSN Hava Durumu sayfasına gidilir
   - Çerezler kabul edilir
   - Ekran görüntüsü alınır
   - Görüntü T100 tablete uygun şekilde işlenir ve kaydedilir
   - İşlenen görüntü tablet ekranında görüntülenir

2. Program çalıştıktan sonra aşağıdaki dosyalar oluşturulur:
   - `msn_eregli.png`: İlk ekran görüntüsü
   - `msn_screen.png`: Tam sayfa ekran görüntüsü
   - `genel_bakis.jpg`: Tablet ekranına özel olarak işlenmiş ve kırpılmış hava durumu görüntüsü

## T100 Tablet Entegrasyonu

- Uygulama, T100 tabletin 1024x600 çözünürlüğüne uygun olarak optimize edilmiştir
- Görüntüler otomatik olarak tabletin çözünürlüğüne uygun şekilde ölçeklendirilir
- Tablet ev girişine monte edilmiştir ve 7/24 çalışır durumdadır
- Enerji verimliliği için düşük güç tüketimine özen gösterilmiştir
- Otomatik başlatma özelliği sayesinde elektrik kesintilerinden sonra bile kendiliğinden çalışmaya devam eder

## Yapılandırma

Kod içerisinde aşağıdaki ayarları değiştirebilirsiniz:
- `setup_driver()` fonksiyonunda tarayıcı ayarları
- `first_selenium_test()` fonksiyonunda hedef URL
- Ekran görüntüsü boyutları ve kırpma alanları

## Katkıda Bulunma

1. Fork'layın
2. Özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi kaydedin (`git commit -am 'Yeni özellik eklendi'`)
4. Dala itin (`git push origin yeni-ozellik`)
5. Pull isteği oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.
