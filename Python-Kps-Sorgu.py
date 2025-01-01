import requests
import json
import urllib3

# InsecureRequestWarning uyarısını bastır
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API URL'si
url = "https://localhost:5011/api/Servis/BilesikKutuk"

# Gönderilecek JSON verisi
data = {
    "kullaniciAdi": "kullaniciAdiniz",
    "sifre": "Şifreniz",
    "kimlikNo": "123123123123",
    "dogumGun": 21,
    "dogumAy": 1,
    "dogumYil": 2003
}

try:
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),
        verify=False
    )

    print("HTTP Durum Kodu:", response.status_code)
    print("Yanıt Metni:", response.text)

    if response.status_code == 200:
        try:
            print("Başarılı JSON Yanıt:", response.json())
        except json.JSONDecodeError:
            print("Yanıt JSON formatında değil.")
    else:
        print(f"HTTP Hatası: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Hata:", e)
