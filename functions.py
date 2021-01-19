import requests
import json
import time

class ChangeOffice():
    def __init__(self):
        self.api_urlUSD = "https://api.exchangeratesapi.io/latest?base=USD"
        self.api_urlEUR = "https://api.exchangeratesapi.io/latest?base=EUR"

    def dovizBoz(self,islem):
        if islem == "dolar":
            response = requests.get(self.api_urlUSD)
            response = json.loads(response.text)
            try:
                bozulan = int(input("Miktar: "))
                result =  int(bozulan * response["rates"]["TRY"])
                print("Güncel Lira karşısında Dolar kuru.",response["rates"]["TRY"] )
                print(f"{bozulan} Dolar {result} TL 'dir.")
            except NameError:
                print("İnternet Bağlantınız Yok, işlem gerçekleştirilemedi...")                
        elif islem == "euro":
            response = requests.get(self.api_urlEUR)
            response = json.loads(response.text)
            try:
                bozulan = int(input("Miktar: "))
                result =  int(bozulan * response["rates"]["TRY"])
                print("Güncel Lira karşısında Euro kuru.",response["rates"]["TRY"] )
                print(f"{bozulan} Euro {result} TL 'dir.")
            except NameError:
                print("İnternet Bağlantınız Yok, işlem gerçekleştirilemedi...")
        
        else:
            pass
        
    def islemler(self):
        while True:
            islem = input("Hangi döviz kurunu bozmak istiyorsunuz -> (dolar,euro) çıkış 'q': ")
            if islem == "q":
                print("Menüye Dönülüyor...")
                time.sleep(1.5)
                break
            if islem == "dolar":
                doviz.dovizBoz(islem)
            elif islem == "euro":
                doviz.dovizBoz(islem)
            else:
                print("hatalı işlem")

doviz = ChangeOffice()

