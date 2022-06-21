n = int(input("Enter Range of Number: "))

n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Please enter a positive integer")

elif n == 1:
   print("Fibonacci Sequence upto",n,":")
   print(n1)

else:
   print("Fibonacci Sequences:")
   while count < n:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1