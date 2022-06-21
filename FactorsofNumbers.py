def checkFactors(n):
   print("The factors of",n,"are:")
   for i in range(1, n + 1):
       if n % i == 0:
           print(i)

n = int(input('Enter Number: '))
checkFactors(n)