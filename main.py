from functions import ChangeOffice
import time

doviz = ChangeOffice()
print("""
            Basit Döviz Kuru V1 
            ₺ $ €
""")

while True:
    print("\nİşlemlere Başlamadan önce kayıt olun...\n")

    time.sleep(0.5)

    sigIn = input("İsim kayıt: ")
    passw = input("şifre kayıt: ")

    
    sigIn2 = input("isminiz: ")
    passw2 = input("şifreniz: ")
      
    if sigIn == sigIn2 and passw != passw2:
        print("şifreniz yanlış")
        continue
    elif passw == passw2 and sigIn != sigIn2:
        print("isminiz yanlış")
        continue
    elif passw == passw2 and sigIn == sigIn2:
        doviz.islemler()
    elif passw != passw2 and sigIn != sigIn2:
        print("her ikiside yanlış")
    elif islem == "çıkış":
        print("Program kapatılıyor...")
        time.sleep(1.5)
        break
    else:
            print("Hatalı İşlem")
