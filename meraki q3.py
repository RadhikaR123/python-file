

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]

obj=open("bank.txt","w")

for i in banks_list:
    value=obj.write(i+'\n')
print("your list is written ...")
obj.close()