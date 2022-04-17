fobj=open("sumofnum.txt","w")

total=0
number=1

for i in range(5):
    num=int(input("enter number :"))
    number=number+i
    total=total+num
    fobj.write(str(num))
    fobj.write('\n')

fobj.write(str(total))

print("total of number is :",total)

fobj.close()
    



