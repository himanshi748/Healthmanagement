

#HEALTH MANAGEMENT SYSTEM

user_name1 = input("Enter your name :")
log = input("Enter Exercise or Diet or retrieve to retrieve file : ")
user_name = user_name1.lower()
userlog = log.lower()

def getdate():
    import datetime
    return datetime.datetime.now()

if userlog == "exercise" :
    f = open(user_name + userlog + ".txt" , "a")
    text = input("enter detail about it : ")
    f.write("["+str(getdate()) +"] :" + text + "\n")
    k = "y"
    while(k != "n"):
            print("enter" , userlog, "\n" , end ="")
            mytext = input()
            f.write("["+str(getdate()) +"] :" + mytext + "\n")
            k = input("add more data y/n ?:")
            continue
    f.close()

elif userlog == "diet" :
    f = open(user_name + userlog + ".txt" , "a")
    text = input("enter detail about it : ")
    f.write("["+str(getdate()) +"] :" + text + "\n")
    k = "y"
    while(k != "n"):
            print("enter" , userlog, "\n" , end ="")
            mytext = input()
            f.write("["+str(getdate()) +"] :" + mytext + "\n")
            k = input("add more data y/n ? :")
            continue
    f.close() 

elif log == "retrieve" :
     data1 = input("enter the file log exercise or diet ? :")
     data = data1.lower()
     f = open(user_name  + data + ".txt" , "rt")
contents = f.readlines()
for line in contents:
    print(line , end = "")
    f.close() 
      
else :
    print("Thanku for your Time ;)")