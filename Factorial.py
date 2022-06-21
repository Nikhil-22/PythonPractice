num = int(input("Enter Number: "))
fact = 1

if num < 0:
   print("Enter Number Greater than 0")

elif num == 0:
   print("The Factorial of 0 is 1")

else:
   for i in range(1,num + 1):
       fact = fact * i
   print("The Factorial of",num,"is",fact)