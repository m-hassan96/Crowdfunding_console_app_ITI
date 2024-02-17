from login import login  
from signup import signup

import os

def mainMenue():
    os.system("clear")
    print(" << =========================================== >>\n")
    print(" <<-- Welcome to our program ^_^ -->> \n ")  
    print(" <<-- Please Login or register for new account -->> ")  
    print(" \n<< ========================================== >>\n")

    while True:    
        print("<<-- PLease Select what you want to do -->> \n ")      
        print(" - 1) Login \n")   
        print(" - 2) Registration \n")  
        chooseInput = input(f" - Please enter your choose: ")
        if chooseInput == "1":
            os.system("clear")
            login()
            return False        
        if chooseInput == "2":
            os.system("clear")
            signup()
            os.system("clear")
            login()
            return False     
        print("\n <<-- Incorrict answer please select 1 or 2 -->> \n ") 
        print(" << ===============================>>\n")
          
mainMenue()