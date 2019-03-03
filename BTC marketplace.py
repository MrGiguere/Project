#Create different wallets for different users
#Create a mine function that gives a set amount of BTC
#Transfer bitcoin between wallets
#Destroy wallet

import random

class Wallet: #Creates the Wallet class
    def __init__(self, password, pin, balance):
        self.password = password
        self.pin = pin
        self.balance = balance

    def checkBalance(self):
        print(self.balance)
    
    def deleteWallet(self, name, password): #deletes a user's wallet
        if name.password == password:
            del name
            print("Deleted.")
        else:
            print("Error wrong password.")

    def transferBitcoin(self,password, amount, address):
        if self.password == password:
            self.balance = self.balance - amount
            address.balance = address.balance + amount
        else:
            print("Error!")

    def mineBitcoin(self, guess):
        number = random.randint(0,6)
        if guess == number:
            balance = balance+1
            print("Your balance has been updated, your wallet contains: "+str(self.balance))

