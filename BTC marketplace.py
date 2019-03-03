##File: project2.py
##Author: Ethan Pafford, Allen Ngo, Max Babka, Eric Zhang
##Date: Due 3/23/2019
##Class: AP Computer Science Principles period 3
##Teacher: Mr. Giguere
##Code Description: Simulate a Bitcoin marketplace (using wallets)

import random

class Wallet: #Creates the Wallet class
    def __init__(self, password, pin, balance):
        self.password = password
        self.pin = pin
        self.balance = balance

    def checkBalance(self): #Checks your balance
        print(self.balance)
    
    def deleteWallet(self, name, password): #deletes a user's wallet
        if name.password == password:
            del name
            print("Deleted.")
        else:
            print("Error wrong password.")

    def transferBitcoin(self,password, amount, address): #Transfers Bitcoin 
        if self.password == password:
            self.balance = self.balance - amount
            address.balance = address.balance + amount
        else:
            print("Error!")

    def mineBitcoin(self, guess): #Mine new Bitcoin
        number = random.randint(0,6)
        if guess == number:
            self.balance = self.balance+1
            print("Your balance has been updated, your wallet contains: "+str(self.balance))
        else:
            print("Your SHA-256 hash was incorrect")

