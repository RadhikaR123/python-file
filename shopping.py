
f=open("shopping.txt","a")
total=0
for i in range(8):
    grocery=input("enter item name :")
    price=int(input("enter their price :"))
    total=total+price
    record=grocery+'-'+str(price)+'\n'

    f.write(record)

f.write(str(total))

f.close()