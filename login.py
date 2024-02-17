from  json_operations import read_data_from_json
from projectsOperation import projectsOperation  
import time
import os

# d_keys = userData[0][4].keys()  # dict_keys
# keys = list(d_keys)
# print(keys)

# d_values = userData[0][4].values()  # dict_values
# values = list(d_values)
# print(values)
# lastID=(len(userData[0]))-1
# newID= len(userData[0])

# keys = list(userData[0][(len(userData[0]))-1].keys())

# values = list(userData[0][(len(userData[0]))-1].values())

#print(f"key={keys[0]},value={values[0]} ")
    
# for i in range(len(userData[0])):
#     keys = list(userData[0][i].keys())
#     values = list(userData[0][i].values())
#     print(f"key={keys[3]},value={values[3]} ")
#     print(f"key={keys[4]},value={values[4]} ")
#     print("")
# for i in range(len(userData[0])):
#     print(f"key={keys[i]},value={values[i]} ")
        
##* checkPassword
def checkUser(Email,Password):        

    userData=[read_data_from_json("Day 3/Project/users.json")]
    global userID
    for i in range(len(userData[0])):
        keys = list(userData[0][i].keys())
        values = list(userData[0][i].values())        
        # print(f"key={keys[3]},value={values[3]} ")
        # print(f"key={keys[4]},value={values[4]} ")
        # print("")
        if  ( Email == values[3] ):
            #print("\n - Your email is true:", Email," >> ")
            userID = int(values[0])
            #print("\n - The user ID",userID," >> ")                        
            if  ( Password == values[4] ):
                #print("\n - Your Password is true: ", Password," >> \n")
                print(" <<-- You are login successfully -->> ")
                time.sleep(2)
                os.system("clear")  
                print(" << =========================================== >>\n")
                print(" <<-- Welcome to our program sir: ", values[1] ,"-->> ")  
                print(" \n << ========================================= >> \n")
                return True
            else:
                    print("\n - your password not correct please enter valid Password :", Password," >> ")
                    return False    
    else:
            print("\n << you are not exist please enter a valid email :", Email," >> ")
            return False            
    
##* check Email
def login():    
    
    print(" << ==========================================> >\n")
    print(" <<-- Welcome to our program ^_^ please login -->> ")  
    print(" \n << ========================================== >>")
    Email = input(f"\n - Please enter your Email: ")
    Password = input(f"\n - Please enter your Password: ")
    print(" << ============================ >>\n")
    
    if checkUser(Email,Password):
        projectsOperation(userID)        
    else:
        login()


if __name__ == "__main__":
    login()
    #CreatProject(2)    
                    
# #* checkConfPassword
# while True:
#     ConfPassword = input(f"\n - Please enter confirm Password: ")
#     #print("Your Password:", Password, type(Password))
#     #print("Your ConfPassword:", ConfPassword, type(ConfPassword))
#     if  ( ConfPassword == Password ):
#         #print("Your ConfPasswordafter:", ConfPassword, type(ConfPassword))
#         break        
#     print("\n <<-- this password not typical write it again -->> ")  

# #* checkMobile
# while True:
#     Mobile = input(f" - Please enter your mobile: ")
#     if re.match(patternMobile, Mobile):
#         #print("Your Name:", Mobile)
#         break        
#     print("\n <<-- please enter valid mobile number -->> ")  

# userData = {"id":1,"Fname":Fname, "Lname":Lname,"Email":Email,"Password":Password,"Mobile":Mobile}

# #save the data on users json
# write_data_to_json("Day 3/Project/users.json", userData)

# print("\n << ============================ >>\n")
# print("<< Thank you for register your data saved >> ")
# print(" \n<< ============================ >>")