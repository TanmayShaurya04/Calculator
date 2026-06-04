x=int(input("Enter your first number:"))
o=input("Enter your Operation:")
y=int(input("Enter your second number:"))

match o:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "/":
        print(x/y)
    case _:
        print("Invalid Operation")