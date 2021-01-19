import requests
import json
import time

class ChangeOffice():
    def __init__(self):
        self.api_urlUSD = "https://api.exchangeratesapi.io/latest?base=USD"
        self.api_urlEUR = "https://api.exchangeratesapi.io/latest?base=EUR"

    def currencyExchange(self,currencyExchange):
        if operation == "dollar":
            response = requests.get(self.api_urlUSD)
            response = json.loads(response.text)
            try:
                quantity = int(input("Quantity: "))
                result =  int(quantity * response["rates"]["TRY"])
                print("Lira rate against Dollar.",response["rates"]["TRY"] )
                print(f"{quantity} Dolar {result} is Lira.")
            except NameError:
                print("No Internet Connection, action could not be performed ...")                
        elif operation == "euro":
            response = requests.get(self.api_urlEUR)
            response = json.loads(response.text)
            try:
                quantity = int(input("Quantity: "))
                result =  int(quantity * response["rates"]["TRY"])
                print("Lira rate against Euro.",response["rates"]["TRY"] )
                print(f"{quantity} Euro {result} is Lira.")
            except NameError:
                print("No Internet Connection, action could not be performed ...")
        
        else:
            pass
        
    def transactions(self):
        while True:
            operation = input("Which exchange rate do you want to break -> (dollar,euro) exit 'q': ")
            if operation == "q":
                print("Returning to the Menu ...")
                time.sleep(1.5)
                break
            if operation == "dollar":
                doviz.currencyExchange(currencyExchange)
            elif operation == "euro":
                doviz.currencyExchange(currencyExchange)
            else:
                print("Incorrect operation")

currency = ChangeOffice()

