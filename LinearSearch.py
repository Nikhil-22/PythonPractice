n = int(input("Enter Number to Store: "))
a = []
f = 0

for i in range(n):
    a.append(int(input()))

x = int(input("Enter Number to Search: "))

for i in range(n):
    if (x==a[i]):
        print("Element {} is Found at Position: ".format(x), i)
        f = 1
        break
if(f==0):
    print("Element Not Found")