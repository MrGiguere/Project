##File: project2.py
##Author: Ethan Pafford, Max Babka, Eric Zhang, Allen Ngo
##Date: Due 3/4/2019
##Class: AP Computer Science Principles period 3
##Teacher: Mr. Giguere
##Code Description: 


#Create different wallets for different users
#Create a mine function that gives a set amount of BTC
#Transfer bitcoin between wallets
#Destroy wallet


class Wallet: #Creates the Wallet class
    def __init__(self,username,password, pin):
        self.username = username
        self.password = password
        self.pin = pin



def deleteWallet(name, password): #deletes a user's wallet
    if name.password == password:
        del name
        print("Deleted.") #correct password, Deleted!
    else:
        print("Error wrong password.") #incorrect password


    



























