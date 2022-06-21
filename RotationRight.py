def printArray(a):
    for k in range(n):
        print(a[k], end=" ")

def rotatebyOne(a):
    temp = a[n-1]

    for v in range(n-1, -1, -1):
        a[v] = a[v-1]
    a[0] = temp

n = int(input("Enter Size of Array : "))
a = []
c = []

print()
print("Enter Elements in Array : ")
for i in range(n):
    a.append(int(input()))

print()
print("Array Before Rotation : ")
printArray(a)

print()
print()
rshift = int(input("Enter Number of Times to Rotate Right : "))
rshift = rshift % 10

for i in range(rshift):
    rotatebyOne(a)

print()
print("Array After Rotation : ")
printArray(a)
print()
