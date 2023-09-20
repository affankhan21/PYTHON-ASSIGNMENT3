num=int(input("ENTER NUMBER OF PERSONS:"))
amt=int(input("ENTER AMOUNT OFTICKET:"))
totalfare=0
for i in range(1,num+1):
    age=int(input("ENTER AGE PERSON:"))   
    if age<12:
        dis= amt * 30/100
    elif age>59:
        dis= amt * 50/100
    else:
        dis=0        
    totalfare +=amt-dis

print("YOUR TOTAL AMOUNT TO PAY IS:",totalfare)
