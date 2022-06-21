def add(x,y):
    print(x+y)

def subtract(x,y):
    print(x-y)

def multiply(x,y):
    print(x*y)

def divide(x,y):
    print(x/y)

n1=int(input("Enter 1st Number: "))
n2=int(input("Enter 2nd Number: "))

op=input("Enter Operation to be Performed +,-,*,/ : ")

if op=='+':
    add(n1, n2)

elif op=='-':
    subtract(n1, n2)

elif op == '*':
    multiply(n1, n2)

elif op=='/':
    divide(n1, n2)

else:
    print("Invalid Entry")