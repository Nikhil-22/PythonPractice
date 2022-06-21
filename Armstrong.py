num = int(input("Enter Number to Check Armstrong or Not: "))
sum = 0

temp = num

while temp > 0:
   digit = temp % 10
   sum += pow(digit,3)
   temp //= 10

if num == sum:
   print(num,"is an Armstrong Number")
else:
   print(num,"is not an Armstrong Number")