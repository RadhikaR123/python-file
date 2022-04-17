

obj1=open("exersice.txt","r")
count=0
str1=" "
while str1:
    str1=obj1.readline()
    print(str1)
    count=count+1
print(count-1)

obj1.close()