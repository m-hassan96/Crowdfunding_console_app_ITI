from  json_operations import write_data_to_json, read_data_from_json
import re, time

patternName = r'^[a-zA-Z_.+-]+$'
patternEmail = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
patternPassword = r'^[a-z A-Z 0-9_\-\@\%\~]{8,20}$'
patternMobile = r'^[0][0-9]{10}$'

def signup():
    
    print(" << ========================================================== >>\n")
    print(" <<-- Welcome to our program please fill out this application carefully  ^_^ -->> ")  
    print(" \n<< ========================================================== >>")

    #* check Fname
    while True:
        Fname = input(f"\n - Please enter your first name: ")
        if re.fullmatch(patternName, Fname):
            #print("Your Name:", Fname)
            break        
        print("\n <<-- please enter name characters only -->> ")  

    #* check Lname
    while True:
        Lname = input(f"\n - Please enter your last name: ")
        if re.fullmatch(patternName, Lname):
            #print("Your Name:", Lname)
            break        
        print("\n <<-- please enter name characters only -->> ")  

    ##* check Email
    while True:
        Email = input(f"\n - Please enter your Email: ")
        if re.fullmatch(patternEmail, Email):
            #print("Your Name:", Email)
            break
        print(" \n<<-- please enter valid email -->> ")    

    ##* checkPassword
    while True:
        Password = input(f"\n - Please enter your Password: ")
        if re.fullmatch(patternPassword, Password):
            #print("Your Password:", Password, type(Password))
            break        
        print("\n <<-- please enter password mix -->> ")  

    #* checkConfPassword
    while True:
        ConfPassword = input(f"\n - Please enter confirm Password: ")
        #print("Your Password:", Password, type(Password))
        #print("Your ConfPassword:", ConfPassword, type(ConfPassword))
        if  ( ConfPassword == Password ):
            #print("Your ConfPasswordafter:", ConfPassword, type(ConfPassword))
            break        
        print("\n <<-- this password not typical write it again -->> ")  

    #* checkMobile
    while True:
        Mobile = input(f"\n - Please enter your mobile: ")
        if re.match(patternMobile, Mobile):
            #print("Your Name:", Mobile)
            break        
        print("\n <<-- please enter valid mobile number -->> ")  

    userData=[read_data_from_json("Day 3/Project/users.json")]
    newID= int(len(userData[0]))

    userData = { "id": newID ,"Fname":Fname, "Lname":Lname,"Email":Email,"Password":Password,"Mobile":Mobile}
    

    #save the data on users json
    write_data_to_json("Day 3/Project/users.json", userData)

    print("\n << ============================ >>\n")
    print("<< Thank you for register your data saved >> ")
    print(" \n<< Now, you will be directed to log in to start your processes >>")
    print(" \n<< ============================ >>")
    time.sleep(2)

if __name__ == "__main__":
    signup()