

obj=open("question4.txt","a")
obj1=open("delhi.txt","a") 
obj2=open("shimla.txt","a")
obj3=open("others.txt","a")


for i in range (1):
    name=input("enter name :")
    city=input("enter city name :")
    value=(name + '-' + city + '\n')
    obj.write(value)
    

    if city=="delhi":  
        obj1.write(value)


    elif city=="shimla":
        obj2.write(value)
    


    else:
        obj3.write(value)


# print("lives in delhi",value)
# print("lives in shimla:",value1)
obj.close()
obj1.close()
obj2.close()
obj3.close()

