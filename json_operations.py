import json

def read_data_from_json(filename):
    try:
        fileobject = open(filename, "r")
    except Exception as e:
        print("Error opening file ")
    else:
        try:
            data = json.load(fileobject)
        except Exception as e:
            data = []
            #print(data, type(data))
            print("Error reading the data and make empty list ")
        fileobject.close()
        return data

def write_data_to_json(filename, userdata ):
    
    old_data=read_data_from_json(filename)
    old_data.append(userdata)
    
    try:
        filobject=  open(filename, mode="w")  # keep old content
    except Exception as e:
        print(e)
        return  False
 
    else:
        json.dump(old_data, filobject, indent=4)
        return  True



if __name__ == "__main__":
    title = input("please enter a book title: ")
    pages = int(input("please enter pages "))
    data = {"name":title, "id":pages}

    #read_data_from_json("Day 3/Project/users.json")
    write_data_to_json("Day 3/Project/users.json", data)
    
    