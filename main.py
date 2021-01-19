from functions import ChangeOffice
import time

currency = ChangeOffice()
print("""
        Simple Exchange Rate V1
            ₺ $ €
""")

while True:
    print("\nRegister Before Starting Transactions ...\n")

    islem = input("Would you like to register?(yes/no/exit): ")
    if islem == "no":
        print("Program kapatılıyor...")
        time.sleep(1.5)
        break
    elif islem == "yes":
        sigInl = []
        passwl = []

        sigIn = input("Name register: ")
        passw = input("Pass register: ")

        sigInl.append(sigIn)
        passwl.append(passw)

        sigIn2 = input("Name: ")
        passw2 = input("Pass: ")
        
        for h in sigInl:
            for j in passwl:
                if sigIn2 != h and passw2 == j:
                    print("Name wrong")
                elif passw2 != j and sigIn2 == h:
                    print("Password wrong")
                elif sigIn2 != h and passw2 != j:
                    print("both wrong")
                elif sigIn2 == h and passw2 == j:
                    currency.transactions()
                else:
                    print("Hatalı İşlem") 
    elif islem == "exit":
        print("program is closing ...")
        time.sleep(1.5)
        break
    else:
        print("Incorrect operation")
