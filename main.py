from art import logo

def add(n1, n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiple(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2==0:
        return "Can't divide with 0"
    return n1/n2

def operators(n1):
    character = input("+\n-\n*\n/\n   Enter the operator")
    n2 = float(input("Enter the Second Number"))
    if character == "+":
        print(add(n1, n2))
        n1=add(n1,n2)
    elif character == "-":
        print(sub(n1, n2))
        n1 = sub(n1, n2)
    elif character == "*":
        print(multiple(n1, n2))
        n1 = multiple(n1, n2)
    elif character == "/":
        print(divide(n1, n2))
        n1 = divide(n1, n2)
    else:
        print("Entered an Invalid Operator-Select Correct operator")
        operators(n1)

    repeat=input(f"Type 'y' to continue calculating with {n1}, or type 'n' to start a new calculation: ").lower()

    if repeat=="y":
        operators(n1)
    else:
        print("\n" * 20)
        calculator()
def calculator():
    print(logo)
    n1=float(input("Enter The First Number"))
    operators(n1)



calculator()