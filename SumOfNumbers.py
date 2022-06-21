number = int(input("Enter Any Numbers: "))
sum = 0

while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits:",sum)