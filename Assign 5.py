#q-1
lowerrange1= input("Enter the lower range")
lowerrange=int(lowerrange1)
upperrange1= input("Enter the upper range")
upperrange=int(upperrange1)
n= int(input("enter the number"))
i= lowerrange+1#to keep the starting and end not included
while i<upperrange:
    if(i%n==0):
        print(i)
    i=i+1


#q-2 
for i in range(1,6):
    for j in range(0,i):
        print('*', end='')
    print()
for i in range(0,5):
    j=4-i
    while(j>0):
        print('*', end='')
        j=j-1
    print()

#q-3
a= input("Enter a string")
b= len(a)
while b>0:
    print(a[b-1], end='')
    b=b-1

#q-4
a= ['dheeraj','dheeraj','vaibhav','gursimar','amisha','vaibhav','kundu','kundu']
for i in a:
    g=0
    n=0
    if(i=='----'):
        continue

    for j in a:
        if(i==j):
            n=n+1
            a[g]='----'
        g=g+1
    print(i," occured ",n," times")
    
            

lowerrange1= input("Enter the lower range")
lowerrange=int(lowerrange1)
upperrange1= input("Enter the upper range")
upperrange=int(upperrange1)
for i in range(lowerrange,upperrange):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i)
        
#Q-6
for i in range (1,500):
    if(i%7==0 and i%11==0):
        print(i)

#Q-7
import math
a=int(input("ENTER THE FIRST SIDE: "))
b=int(input("ENTER THE second SIDE: "))
c=int(input("ENTER THE third SIDE: "))
s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of the triangle: ',area)

