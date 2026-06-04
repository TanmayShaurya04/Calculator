name=input("Enter your name: ") #for loop 
for i in name:  #i is a variable that takes each character of the string "name" one by one and prints it
    print(i)

name=input("Enter your name: ")
for i in name:
    print(i, end=" ")


#range(x,y,z) x is the starting point, y is the ending point and z is the step size
# like x is your initialization y is condition and z is updation 0 to n-1

for i in range(0,11,1):  #prints numbers from 10 to 1
    print(i)  #prints numbers from 0 to 9
 #IF YOU USE RANGE() with one variable that means it understood that i=0 and updation is one you only need to put codn for termination

 #IF YOU USE RANGE() WITH TWO VARIABLES THAT MEANS IT UNDERSTOOD THAT UPDATION CODN IS 1 AND YOU HAVE TO PUT CODN FOR INITIALIZATION AND TERMINATION  
num=int(input("input n: "))
totalsum=0
for i in range (1,num+1):
    totalsum=totalsum+i
print(totalsum)


#imp q

name=input("input string:")
name=name.lower()
count=0
for i in name:
    if(i in "aeiou"):
        count=count+1
    else:
        continue
print(count)   

#prime not prime
num=12
count=0
for i in range(1,num+1,1):
    if(num%i==0):
        count=count+1
if(count==2):
      print("prime")
else:
      print("not prime")


      #login method 
attempts=0
password="tanmay"
user=0
while True:
    user=input("input password: ")
    if(password != user):
        attempts=attempts+1
    else:
        print("LOGGED IN")
        break
    if(attempts==3):
       print("Account locked")        
       break
     