from functions import ChangeOffice
import time

doviz = ChangeOffice()
print("""
            Basit Döviz Kuru V1 
            ₺ $ €
""")

while True:
    print("\nİşlemlere Başlamadan önce kayıt olun...\n")

    islem = input("Kayıt Olmak İstermisiniz?(evet/hayır/çıkış): ")
    if islem == "hayır":
        time.sleep(0.5)
    elif islem == "evet":
        sigInl = []
        passwl = []

        sigIn = input("İsim kayıt: ")
        passw = input("şifre kayıt: ")

        sigInl.append(sigIn)
        passwl.append(passw)

        sigIn2 = input("isminiz: ")
        passw2 = input("şifreniz: ")
        
        for h in sigInl:
            for j in passwl:
                if sigIn2 != h and passw2 == j:
                    print("İsim yanlış")
                elif passw2 != j and sigIn2 == h:
                    print("şifreniz Yanlış")
                elif sigIn2 != h and passw2 != j:
                    print("Her ikiside Yanlış")
                elif sigIn2 == h and passw2 == j:
                    doviz.islemler()
                else:
                    print("Hatalı İşlem") 
    elif islem == "çıkış":
        print("Program kapatılıyor...")
        time.sleep(1.5)
        break
    else:
        print("Hatalı İşlem")
