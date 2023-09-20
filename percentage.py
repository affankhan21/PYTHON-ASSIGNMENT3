stud=int(input("ENTER NUMBER OF STUDENTS YOU WANT: "))
a=stud
sum1=0
while(a!=0):
    for i in range(1,6):
        marks=int(input("ENTER MARKS FOR SUBJECT:"))
        sum1+=marks
    avgperc=sum1/5
    perc=(sum1/500)*100
    print("YOUR  AVERAGE PERCENTAGE IS :",avgperc)
    
    print("YOUR   PERCENTAGE IS :",perc)
   
    
    a=a-1

