def printArray(a):
    for k in range(n):
        print(a[k], end=" ")

def rotatebyOne(a):
    temp = a[0]

    for v in range(n-1):
        a[v] = a[v+1]
    a[n-1] = temp


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
lshift = int(input("Enter Number of Times to Rotate Left : "))
lshift = lshift % 10

for i in range(lshift):
    rotatebyOne(a)

print()
print("Array After Rotation : ")
printArray(a)
print()
