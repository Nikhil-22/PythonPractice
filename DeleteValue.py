numbers = int(input("Enter Number to Store: "))
arr = []

for i in range(numbers):
    arr.append(int(input()))
print(arr, end=" ")

print()

x = int(input("Enter Position of an Element you want to Delete: "))

arr.pop(x)
print(arr, end=" ")
