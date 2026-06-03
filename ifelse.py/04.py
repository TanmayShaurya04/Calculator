year=int(input("Enter thr year: "))
if(year%400 == 0 and year%4 == 0 or year%100 !=0 ):
    print("Year is a leap year")
else:
    print("Year uis niot a leap year")