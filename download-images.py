"""
Han Oto Dizayn — Instagram Galeri Fotoğrafları İndirme Scripti
--------------------------------------------------------------
Kullanım:
  1. Terminal açın
  2. 'han-oto-dizayn' klasörüne gidin:
       cd ~/han-oto-dizayn   (ya da neredeyse oraya gelin)
  3. Scripti çalıştırın:
       python3 download-images.py

Fotoğraflar images/gallery/ klasörüne kaydedilir.
"""

import urllib.request
import os
import time

GALLERY_DIR = os.path.join(os.path.dirname(__file__), "images", "gallery")
os.makedirs(GALLERY_DIR, exist_ok=True)

IMAGES = {
    "direksiyon_1.jpg": "https://instagram.fsaw1-13.fna.fbcdn.net/v/t51.82787-15/561834864_18071735072230290_963617534037469871_n.jpg?stp=c0.292.750.750a_dst-jpg_e15_s640x640_tt6&_nc_ht=instagram.fsaw1-13.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2gGGSkL7KKuv9CqMqW5Zxpk_A2RYrieUY_pcM6jE_EC4J9ZKucBs9stF5cV2gCDliZQ&_nc_ohc=3xhmQHUQs1gQ7kNvwFQpuuf&_nc_gid=BPu7pmrDSuwCl_l9mmZfBg&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af2z3O71O2QvWAgVkA0PDmpwto_bdvbAO-mBYb7H1Utidw&oe=69F11AD3&_nc_sid=94fea1",
    "kapi_1.jpg":       "https://instagram.fsaw1-15.fna.fbcdn.net/v/t51.71878-15/557546725_2344480282652645_7082861996347508184_n.jpg?stp=c0.248.640.640a_dst-jpg_e15_tt6&_nc_ht=instagram.fsaw1-15.fna.fbcdn.net&_nc_cat=105&_nc_oc=Q6cZ2gGGSkL7KKuv9CqMqW5Zxpk_A2RYrieUY_pcM6jE_EC4J9ZKucBs9stF5cV2gCDliZQ&_nc_ohc=VD3bMjGl0AUQ7kNvwGcVECf&_nc_gid=BPu7pmrDSuwCl_l9mmZfBg&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af3XY0c_jVBxWna2C9N72miYrB6JUrhXl-BiCs0ww51eJg&oe=69F12A0C&_nc_sid=94fea1",
    "koltuk_1.jpg":     "https://instagram.fsaw1-13.fna.fbcdn.net/v/t51.71878-15/568100353_688365554310391_4735433010118570031_n.jpg?stp=c0.248.640.640a_dst-jpg_e15_tt6&_nc_ht=instagram.fsaw1-13.fna.fbcdn.net&_nc_cat=107&_nc_oc=Q6cZ2gGGSkL7KKuv9CqMqW5Zxpk_A2RYrieUY_pcM6jE_EC4J9ZKucBs9stF5cV2gCDliZQ&_nc_ohc=wD8VVj0oNUEQ7kNvwGZEiuB&_nc_gid=BPu7pmrDSuwCl_l9mmZfBg&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af0XpiKDeNhzNfEsuJTfnGslFPi1o2ZFf6ZU_8aG59xs8g&oe=69F12035&_nc_sid=94fea1",
    "koltuk_2.jpg":     "https://instagram.fsaw1-15.fna.fbcdn.net/v/t51.71878-15/588727459_1431989038454032_3908962337723334058_n.jpg?stp=c0.248.640.640a_dst-jpg_e15_tt6&_nc_ht=instagram.fsaw1-15.fna.fbcdn.net&_nc_cat=104&_nc_oc=Q6cZ2gGGSkL7KKuv9CqMqW5Zxpk_A2RYrieUY_pcM6jE_EC4J9ZKucBs9stF5cV2gCDliZQ&_nc_ohc=h7mnOcjeJFoQ7kNvwHtydiI&_nc_gid=BPu7pmrDSuwCl_l9mmZfBg&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af0hPlyd8lZ-QEwiuvh64sGHYNkjCnXxJJF8lnGXzfyHWw&oe=69F1204B&_nc_sid=94fea1",
    "tavan_1.jpg":      "https://instagram.fsaw1-15.fna.fbcdn.net/v/t51.71878-15/571382420_1557976498541381_8996856125552372198_n.jpg?stp=c0.248.640.640a_dst-jpg_e15_tt6&_nc_ht=instagram.fsaw1-15.fna.fbcdn.net&_nc_cat=105&_nc_oc=Q6cZ2gGGSkL7KKuv9CqMqW5Zxpk_A2RYrieUY_pcM6jE_EC4J9ZKucBs9stF5cV2gCDliZQ&_nc_ohc=_nM22-rTRgcQ7kNvwGdKqwc&_nc_gid=BPu7pmrDSuwCl_l9mmZfBg&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af3qtj7xB9JPLnPBlwG0IMcd-uyp-8dls0TMp_u-yW_59w&oe=69F10F14&_nc_sid=94fea1",
    "taban_1.jpg":      "https://instagram.fsaw1-13.fna.fbcdn.net/v/t51.82787-15/573054762_18131999389485894_1768292002716957205_n.jpg?stp=c0.292.750.750a_dst-jpg_e15_s640x640_tt6&_nc_ht=instagram.fsaw1-13.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2gGGSkL7KKuv9CqMqW5Zxpk_A2RYrieUY_pcM6jE_EC4J9ZKucBs9stF5cV2gCDliZQ&_nc_ohc=kMYBtiESMxIQ7kNvwH1PpBR&_nc_gid=BPu7pmrDSuwCl_l9mmZfBg&edm=AGW0Xe4BAAAA&ccb=7-5&oh=00_Af12Ej_Y9ioX5bjG8rGNejABlQ-PhmYPtrMRq2kNhtq_mg&oe=69F124F0&_nc_sid=94fea1",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": "https://www.instagram.com/",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
}

print("=" * 50)
print("Han Oto Dizayn — Galeri Fotoğrafları İndiriliyor")
print("=" * 50)

ok, skip, fail = 0, 0, 0

for filename, url in IMAGES.items():
    dest = os.path.join(GALLERY_DIR, filename)

    if os.path.exists(dest) and os.path.getsize(dest) > 1024:
        print(f"⏭  Zaten mevcut: {filename}")
        skip += 1
        continue

    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        size_kb = len(data) // 1024
        print(f"✓  İndirildi: {filename}  ({size_kb} KB)")
        ok += 1
        time.sleep(0.5)  # Instagram rate-limit aşmamak için
    except Exception as e:
        print(f"✗  Hata ({filename}): {e}")
        fail += 1

print()
print(f"Tamamlandı: {ok} indirildi, {skip} atlandı, {fail} hata")
if ok > 0:
    print("→ Tarayıcıda index.html'i yenileyin, resimler görünecek.")
if fail > 0:
    print("→ Hatalı URL'lerin süresi dolmuş olabilir. Yeni JSON gönderin.")
