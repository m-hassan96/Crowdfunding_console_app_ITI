from  json_operations import write_data_to_json, read_data_from_json
import re, os, time, json

patternName = r'^[a-zA-Z0-9_.+-]+$'
patternDate = r'^\d{4}-\d{2}-\d{2}$'


#* to create your projects
def CreatProject(userID):
    
    print(" << ============================ >>\n")
    print(" <<-- Welcome to creating project page -->> ")  
    print(" \n<< ============================ >>")

    #* check title
    while True:
        Title = input(f"\n - Please enter your project title: ")
        if re.fullmatch(patternName, Title):
            #print("Your Name:", Title)
            break        
        print("\n <<-- please enter title name characters only -->> ")  

    #* check details
    while True:
        Details = input(f"\n - Please enter project details: ")
        if Details != "":
            #print("Your Name:", Details)
            break        
        print("\n <<-- please enter valid characters only -->> ")  

    ##* check TotalTarget
    while True:
        TotalTarget = input(f"\n - Please enter your total Target: ")
        if TotalTarget.isdigit():
            #print("Your TotalTarget:", TotalTarget)
            break
        print(" \n<<-- please enter valid TotalTarget number -->> ")    

    ##* check StartDate
    while True:
        StartDate = input(f"\n - Please enter your StartDate: ")
        if re.fullmatch(patternDate, StartDate):
            #print("Your Password:", Password, type(Password))
            break        
        print("\n <<-- please enter valid Date (Y-M-D) -->> ")  

    #* check EndDate
    while True:
        EndDate = input(f"\n - Please enter your EndDate: ")
        #print("Your Password:", Password, type(Password))
        #print("Your ConfPassword:", ConfPassword, type(ConfPassword))
        if re.fullmatch(patternDate, EndDate):
            #print("Your ConfPasswordafter:", ConfPassword, type(ConfPassword))
            break        
        print("\n <<-- please enter valid Date (Y-M-D)  -->> ")  

    projectData = {"id": userID,"Title":Title, "Details":Details,"TotalTarget":TotalTarget,"StartDate":StartDate,"EndDate":EndDate}
    
    #save the data on projects json
    write_data_to_json("Day 3/Project/projects.json", projectData)

    print("\n << ============================ >>\n")
    print("<< Thank you  your project saved successfully >> ")
    print(" \n<< ============================ >>")
    time.sleep(2)
    
#&---------------------------------------------------------------------------------------------------------------------------   
    
#* to list the projects for specific user    
def ViewProjects(userID):        
    
    projectData=[read_data_from_json("Day 3/Project/projects.json")]
    #print(" \n<< ============================ >>\n")
    #print("user id: ", userID)
    for i in range(len(projectData[0])):        
        #print("projectData len: ", len(projectData[0]))
        keys = list(projectData[0][i].keys())
        values = list(projectData[0][i].values())        
        if  ( userID == values[0] ):
            print(" \n<< ============================ >>")
            print("\n - Your project Title:", values[1])
            print("\n - Your project Details:", values[2])
            print("\n - Your project Total target:", values[3])
            print("\n - Your project Start Date:", values[4])
            print("\n - Your project End Date:", values[5])  
            print(" \n<< ============================ >>")
    
#&---------------------------------------------------------------------------------------------------------------------------   
    
#* to ViewAllProjects
def ViewAllProjects():        
    
    projectData=[read_data_from_json("Day 3/Project/projects.json")]
    for i in range(len(projectData[0])):
        keys = list(projectData[0][i].keys())
        values = list(projectData[0][i].values())       
        print(" \n<< ============================ >>")
        print("\n - The project Title:", values[1])
        print("\n - The project Details:", values[2])
        print("\n - The project Total target:", values[3])
        print("\n - The project Start Date:", values[4])
        print("\n - The project End Date:", values[5])  
        print(" \n<< ============================ >>")                      
    
    time.sleep(2)

#&---------------------------------------------------------------------------------------------------------------------------   

#* to edite the project content  
def EditeProjects(userID):        
    
    projectData=[read_data_from_json("Day 3/Project/projects.json")]    
    
    print(" \n<< ============== want to edit your data ============== >>\n")
    # print("user id: ", userID)
    # print("len of data", len(projectData[0]))
    for i in range(len(projectData[0])):        
        #print("projectData len: ", len(projectData[0]))
        keys = list(projectData[0][i].keys())
        #print("keys: ", keys)
        values = list(projectData[0][i].values()) 
        #print("values: ", values) 
        if  ( userID == values[0] ):
            print(" \n<< ============================ >>")
            print("\n - Your project Title:", values[1])
            print("\n - Your project Details:", values[2])
            print("\n - Your project Total target:", values[3])
            print("\n - Your project Start Date:", values[4])
            print("\n - Your project End Date:", values[5])  
            print(" \n<< ============================ >>")   
        
    print("\n <<-- PLease Select which project you want to edit -->> \n")   
    projectTitle = input(f"\n - Please enter project title: ")
    # print("\n - Your project title:", projectTitle , type(projectTitle))  
    # print("user id: ", userID)
    # print("len of data", len(projectData[0]))
    print(" \n<< ============================ >>")    
    for i in range(len(projectData[0])):        
        #print("projectData len: ", len(projectData[0]))
        
        keys = list(projectData[0][i].keys())
        #print("keys: ", keys)
        values = list(projectData[0][i].values()) 
        #print("values: ", values) 
        if  ( userID == values[0] and projectTitle == values[1]):
            print(" \n<< ============================ >>")
            print("\n - Your project Title:", values[1])
            print("\n - Your project Details:", values[2])
            print("\n - Your project Total target:", values[3])
            print("\n - Your project Start Date:", values[4])
            print("\n - Your project End Date:", values[5])  
            print(" \n<< ============================ >>")  
            
            print("\n - Please select which part you want to edit : \n")
            print(" - 1) Title \n")   
            print(" - 2) Details \n")
            print(" - 3) Total target \n")    
            print(" - 4) Start Date \n")  
            print(" - 5) End Date \n")  
            print(" - 6) Back to menu \n") 
            
            projectPart = int(input(f"\n - Please enter your choose: "))
            
            if projectPart == 1:
                while True:
                    Title = input(f"\n - Please enter your project title: ")
                    if re.fullmatch(patternName, Title): 
                        updateData(i, keys[1] ,Title) 
                        print("\n <<-- wait will direct you back menu -->> ") 
                        time.sleep(2)
                        os.system("clear")
                        projectsOperation(userID)    
                        break
                    print("\n <<-- please enter title name characters only -->> ") 
                #os.system("clear")
                break        
            
            if projectPart == 2:
                while True:
                    Details = input(f"\n - Please enter project details: ")
                    if Details != "":
                        updateData(i, keys[2] ,Details)
                        print("\n <<-- wait will direct you back menu -->> ") 
                        time.sleep(2)
                        os.system("clear")
                        projectsOperation(userID)    
                        break
                    print("\n <<-- please enter valid characters only -->> ")  
                #os.system("clear")
                break      
            
            if projectPart == 3:
                while True:
                    TotalTarget = input(f"\n - Please enter your total Target: ")
                    if TotalTarget.isdigit():                        
                        updateData(i, keys[3] ,TotalTarget) 
                        print("\n <<-- wait will direct you back menu -->> ") 
                        time.sleep(2)
                        os.system("clear")
                        projectsOperation(userID)      
                        break 
                    print(" \n<<-- please enter valid TotalTarget number -->> ")    

                #os.system("clear")
                break      
            
            if projectPart == 4:
                while True:
                    StartDate = input(f"\n - Please enter your StartDate: ")
                    if re.fullmatch(patternDate, StartDate):
                        updateData(i, keys[4] ,StartDate)    
                        print("\n <<-- wait will direct you back menu -->> ") 
                        time.sleep(2)
                        os.system("clear")
                        projectsOperation(userID)    
                        break
                    print("\n <<-- please enter valid Date (Y-M-D) -->> ")  

                #os.system("clear")
                break      
            
            if projectPart == 5:
                
                while True:
                    EndDate = input(f"\n - Please enter your EndDate: ")
                    if re.fullmatch(patternDate, EndDate):                        
                        updateData(i, keys[5] ,EndDate)      
                        print("\n <<-- wait will direct you back menu -->> ") 
                        time.sleep(2)
                        os.system("clear")
                        projectsOperation(userID)    
                        break
                    print("\n <<-- please enter valid Date (Y-M-D)  -->> ") 
                #os.system("clear")
                break    
            
            if projectPart == 6:              
                print("\n <<-- wait will direct you back menu -->> ")                 
                time.sleep(2)
                os.system("clear")
                EditeProjects(2)
                #os.system("clear")
                break
            else:                      
                print("\n <<-- wait will direct you back menu -->> ") 
                time.sleep(2)
                os.system("clear")
                EditeProjects(2)
                   
def updateData(index,key,newData):
    file_path='Day 3/Project/projects.json'
    with open(file_path, 'r', encoding='utf-8') as json_file:
        employees_list = json.load(json_file)

    #print(employees_list)
    employees_list[index][key] = newData
    #print(employees_list[index])

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(employees_list, json_file, indent=4)
        print("\n << ============================ >>\n")
        print("<< Thank you  your project updated successfully >> ")
        print(" \n<< ============================ >>")  
    
#&---------------------------------------------------------------------------------------------------------------------------   
    
#* to delete the project content  
def  DeleteProject(userID):        
    
    projectData=[read_data_from_json("Day 3/Project/projects.json")]    
    
    print(" \n<< ============== want to edit your data ============== >>\n")
    # print("user id: ", userID)
    # print("len of data", len(projectData[0]))
    for i in range(len(projectData[0])):        
        #print("projectData len: ", len(projectData[0]))
        keys = list(projectData[0][i].keys())
        #print("keys: ", keys)
        values = list(projectData[0][i].values()) 
        #print("values: ", values) 
        if  ( userID == values[0] ):
            print(" \n<< ============================ >>")
            print("\n - Your project Title:", values[1])
            print("\n - Your project Details:", values[2])
            print("\n - Your project Total target:", values[3])
            print("\n - Your project Start Date:", values[4])
            print("\n - Your project End Date:", values[5])  
            print(" \n<< ============================ >>")   
        
    print("\n <<-- PLease Select which project you want to delete -->> \n")   
    projectTitle = input(f"\n - Please enter project title: ")
    print(" \n<< ============================ >>")    
    
    for i in range(len(projectData[0])):        
        #print("projectData len: ", len(projectData[0]))
        
        keys = list(projectData[0][i].keys())
        #print("keys: ", keys)
        values = list(projectData[0][i].values()) 
        #print("values: ", values) 
        if  ( userID == values[0] and projectTitle == values[1]):
            print(" \n<< ============================ >>")
            print("\n - Your project Title:", values[1])
            print("\n - Your project Details:", values[2])
            print("\n - Your project Total target:", values[3])
            print("\n - Your project Start Date:", values[4])
            print("\n - Your project End Date:", values[5])  
            print(" \n<< ============================ >>")      
            print("\n << is this project that want to delete >>  \n")
            print(" - 1) Yes \n")   
            print(" - 2) No \n")
            
            projectDelete = int(input(f" -  Please enter your choose: "))            
            if projectDelete == 1:
                deleteData(i) 
                print("\n <<-- wait will direct you back menu -->> ") 
                time.sleep(2)
                os.system("clear")
                projectsOperation(userID)    
                break
            else:                      
                print("\n <<-- wait will direct you back menu -->> ")                 
                time.sleep(2)
                os.system("clear")
                projectsOperation(userID)
                
def deleteData(index):
    file_path='Day 3/Project/projects.json'
    with open(file_path, 'r', encoding='utf-8') as json_file:
        employees_list = json.load(json_file)

    #rint(employees_list)
    del employees_list[index]
    #print(employees_list[index])

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(employees_list, json_file, indent=4)
        print("\n << ============================ >>\n")
        print("<< Thank you  your project deleted successfully >> ")
        print(" \n<< ============================ >>")  
    
#&---------------------------------------------------------------------------------------------------------------------------   
    
#* to search in the project content  

def SearchProjects(userID):        
    
    projectData=[read_data_from_json("Day 3/Project/projects.json")]    
    
    print(" \n<< ============== want to search about your data ============== >>\n")
    # print("user id: ", userID)
    # print("len of data", len(projectData[0]))
    for i in range(len(projectData[0])):        
        #print("projectData len: ", len(projectData[0]))
        keys = list(projectData[0][i].keys())
        #print("keys: ", keys)
        values = list(projectData[0][i].values()) 
        #print("values: ", values) 
        if  ( userID == values[0] ):
            print(" \n<< ============================ >>")
            print("\n - Your project Title:", values[1])
            print("\n - Your project Details:", values[2])
            print("\n - Your project Total target:", values[3])
            print("\n - Your project Start Date:", values[4])
            print("\n - Your project End Date:", values[5])  
            print(" \n<< ============================ >>")   
        
    print("\n <<-- PLease enter what you want to search about it -->> \n")   
    searchWord = input(f"\n - Please enter to search: ")
    print(" \n<< ============================ >>")   
    
    for i in range(len(projectData[0])):        
        #print("projectData len: ", len(projectData[0]))
        keys = list(projectData[0][i].keys())
        print("keys: ", keys)
        values = list(projectData[0][i].values()) 
        print("values: ", values) 
        if  ( userID == values[0]):           
            for j in range(6):                    
                if  ( searchWord.find(str(values[j]))):
                    print(" \n<< ======= Your search about this project ========= >>")
                    print("\n - Your project Title:", values[1])
                    print("\n - Your project Details:", values[2])
                    print("\n - Your project Total target:", values[3])
                    print("\n - Your project Start Date:", values[4])
                    print("\n - Your project End Date:", values[5])  
                    print(" \n<< ============================ >>")             
                    
            print("\n <<-- wait will direct you back menu -->> ") 
            time.sleep(4)
            #EditeProjects( 2)   
            break
#&---------------------------------------------------------------------------------------------------------------------------   
                
#* projectsOperation                                    
def projectsOperation(userID):
    
    #print("user id: ", userID)

    print("\n  <<-- Welcome to our projects Operation ^_^ -->> ")  
    print(" \n<< ==================================== >> \n")

    while True:    
        print("\n <<-- PLease Select what you want to do -->> \n")      
        print(" - 1) View All Projects \n")   
        print(" - 2) View your projects \n")
        print(" - 3) Create your projects \n")    
        print(" - 4) Edite your projects \n")  
        print(" - 5) Delete your projects \n")  
        print(" - 6) Search \n")  
        print(" - 7) Exit \n")    
                
        chooseInput = input(f"\n - Please enter your choose: ")
        if chooseInput == "1":
            os.system("clear")
            print(" \n<< ==================================== >> \n")
            print(" <<--    These are all projects  -->> ")  
            ViewAllProjects()
            projectsOperation(userID)
            #os.system("clear")
            break        
        if chooseInput == "2":
            os.system("clear")
            print(" \n<< ==================================== >> \n")
            print(" <<--    These are your projects     -->> ")  
            ViewProjects(userID)
            projectsOperation(userID)
            #os.system("clear")
            break    
        if chooseInput == "3":
            os.system("clear")
            CreatProject(userID)
            projectsOperation(userID)
            #os.system("clear")
            break    
        if chooseInput == "4":
            os.system("clear")
            print(" <<--    These are your projects     -->> ")  
            EditeProjects(userID)
            projectsOperation(userID)
            #os.system("clear")
            break    
        if chooseInput == "5":
            os.system("clear")
            DeleteProject(userID)
            projectsOperation(userID)
            #os.system("clear")
            break    
        if chooseInput == "6":
            os.system("clear")
            SearchProjects(userID)
            projectsOperation(userID)
            #os.system("clear")
            break    
        if chooseInput == "7":
            os.system("clear")
            print(" \n<<     Okay goodbye see you latter  ^_^    >>\n")
            time.sleep(1)
            exit()
        else:            
            print("\n <<-- Incorrict answer please select corrict answer -->> \n ") 
            print(" << ===============================>>\n")

if __name__ == "__main__":
    
    #CreatProject(2)    

    ViewProjects(2)    