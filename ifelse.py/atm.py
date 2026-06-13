#atm menu
balance =100000 #from database
pin = 1234 #from database
print("Welcome to the ATM")
print("1.Check Balance")
print("2.Deposit Balance")
print("3.Withdraw Balance")
print("4.Change PIN")

choice=int(input("Enter your choice: "))
if(choice == 1):
    print("Your balance is:" , balance)
elif(choice==2):
    deposit=float(input("Enter deposit balance:"))
    balance=balance+deposit
    print("Your new balance is",balance)
elif(choice==3):
    withdraw=float(input("Enter amount to withdraw:"))
    if(balance>= withdraw):
      balance=balance-withdraw
      print("Your new balance is:", balance)
    else:
      print("Insufficient Balance")
else:     
    print("Enter you old PiN: ")
    old_pin=int(input())
    if(old_pin == pin):
        print("Input your New PIN")
        new_pin=int(input())
        print("PIN changed")
    else:
        print("Invalid PIN")