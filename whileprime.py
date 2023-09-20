num =  int(input("Enter a number "))

i=1
count = 0
while count != num:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        if i!=1:
            count+=1
            print(i,end=" ")
    i+=1

print("\nCount = ",count)