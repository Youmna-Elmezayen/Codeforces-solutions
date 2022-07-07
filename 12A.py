matrix = []

for i in range(3):
    matrix.append(input())

# if the first row is the same as the last in reverse and each other cell is equivalent to adjacent cell on opposite side, then it is centered
if(matrix[0] == matrix[2][::-1] and matrix[0][0] == matrix[2][2] and matrix[1][0] == matrix[1][2] and matrix[2][0] == matrix[0][2]):
    print("YES")
else:
    print("NO")