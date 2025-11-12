from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

def setup_driver():
    """    Edge driver'ı otomatik kurar ve ayarlar  """
    # Edge options (ayarlar)
    options = webdriver.EdgeOptions()
    options.add_argument('--start-maximized')  # Pencereyi büyüt
    options.add_argument('--disable-notifications')  # Bildirimleri kapat
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Driver'ı başlat (Selenium 4.6+ sürücüyü otomatik yönetir)
    driver = webdriver.Edge(options=options)
    
    # Bekleme süresi ayarı
    driver.implicitly_wait(10)  # Element bulunana kadar max 10 saniye bekle
    
    driver.save_screenshot("msn_eregli.png")
    time.sleep(2)

    return driver

def first_selenium_test():
    """     İlk Selenium testimiz - Google'da arama yapma       """
    driver = setup_driver()
    print("D032.driver = setup_driver()")

    try:
        #1. sayfasına git
        driver.get("https://www.msn.com/tr-tr/havadurumu/havadurumutahmini/in-Eregli,Zonguldak")
        print("D037.Sayfa açıldı")

        # Çerez (cookie) onayını otomatik olarak kabul et
        try:
            # Butonun tıklanabilir olmasını 5 saniye bekle
            accept_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_button.click()
            print("D046.Çerez onayı kabul edildi.")
            
            # Biraz bekleme ekleyelim
            time.sleep(1)
            
            # "Saatlik" yazısını bul ve en üste kaydır
            try:
                saatlik_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Saatlik')]"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", saatlik_element)
                print("D057.Sayfa 'Saatlik' yazısına kaydırıldı")
                time.sleep(1)  # Kaydırma işleminin tamamlanması için bekle
            except Exception as e:
                print(f"D060.Saatlik' yazısı bulunamadı veya kaydırılamadı: {e}")
            
            # Ekran görüntüsü almadan önce biraz daha bekle
            time.sleep(1)
        except Exception as e:
            print(f"D065.Çerez onayı penceresi bulunamadı veya bir hata oluştu: {e}")
        
        #6. Sayfa başlığını yazdır
        print(f"D068.Sayfa başlığı: {driver.title}")
        time.sleep( 5)
        #7. Ekran görüntüsü al ve işle
        from PIL import Image
        script_dir = os.path.dirname(__file__)
        
        # Tam ekran görüntüsünü al
        full_screenshot = os.path.join(script_dir, "msn_screen.png")
        driver.save_screenshot(full_screenshot)
        print(f"D077.Tam ekran görüntüsü alındı: {full_screenshot}")
        
        # Belirtilen koordinatlarla kırpma işlemi
        try:
            # Verdiğiniz koordinatları kullanıyoruz
            left, top = 171, 154
            right, bottom = 1422, 613
            
            # Görüntüyü aç ve kırp
            img = Image.open(full_screenshot)
            genel_bakis_img = img.crop((left, top, right, bottom))
            
            # 1024x 600 boyutuna yeniden boyutlandır
            genel_bakis_img = genel_bakis_img.resize(( 1024, 600), Image.LANCZOS)
            
            # Kırpılmış görüntüyü kaydet
            genel_bakis_path = os.path.join(script_dir, "genel_bakis.jpg")
            genel_bakis_img.save(genel_bakis_path, "JPEG", quality=95)
            print(f"D095.Genel Bakış kutusu kaydedildi: {genel_bakis_path}")
            
        except Exception as e:
            print(f"D098.Kırpma işlemi sırasında hata oluştu: {e}")
        
    except Exception as e:
        print(f"D101.ERROR Hata: {e}")
    
    finally:
        # Tarayıcıyı kapat
        time.sleep(2)
        driver.quit()
        print("D107.Tarayıcı kapatıldı")
# Çalıştır
first_selenium_test()