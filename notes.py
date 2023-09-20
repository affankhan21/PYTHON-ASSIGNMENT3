
amt=int(input("ENTER THE AMOUNT:"))
total=0


dat=[2000,500,100,50,20,10,5]
for x in dat:
    total=total+amt//x
    amt=amt%x
print("TOTAL NUMBER OF NOTES :",total)   
