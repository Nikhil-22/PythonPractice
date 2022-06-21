def binarySearch(arr, low, high, x):
    if (high >= low):
        mid = (high + low)//2

        if (arr[mid] == x):
            return mid

        elif (arr[mid] > x):
            return binarySearch(arr, low, mid-1, x)

        else:
            return binarySearch(arr, mid+1, high, x)
    else:
        return -1


numbers = int(input("Enter Number to Store: "))
arr = []

for i in range(numbers):
    arr.append(int(input()))

x = int(input("Enter Number to be Search: "))

result = binarySearch(arr, 0, numbers-1, x)

if (result != -1):
    print("Element is Found")
else:
    print("Element not Found")