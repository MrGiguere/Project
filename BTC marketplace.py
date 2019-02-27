#Create different wallets for different users
#Create a mine function that gives a set amount of BTC
#Transfer bitcoin between wallets
#Destroy wallet

import random

class Wallet: #Creates the Wallet class
    def __init__(self,username,password, pin, balance):
    self.username = username
    self.password = password
    self.pin = pin
    self.balance = balance



def deleteWallet(name, password): #deletes a user's wallet
    if name.password == password:
        del name
        print("Deleted.")
    else:
        print("Error wrong password.")

def transferWallet(name, password, amount, address):
    if name.password == password:
        self.balance = self.balance - amount
        address.balance = address.balance + amount

def mineBTC(import('guess a number between 0 & 5')
    number = random.randint(0,6)
    if import() = number
            
    


















