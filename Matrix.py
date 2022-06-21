R = int(input("Enter the Number of Rows: "))
C = int(input("Enter the Number of Columns: "))

matrix = []

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()