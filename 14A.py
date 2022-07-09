n, m = input().split(" ")
matrix = []
imin, imax = int(n), -1
jmin, jmax = int(m), -1

for i in range(int(n)):
    row = input()
    matrix.append(row)
    for j in range(len(row)):
        if row[j] == '*': # if row has *, check the min index for this * element in terms of i and j
            if i < imin:
                imin = i
            if i > imax:
                imax = i
            if j < jmin:
                jmin = j
            if j > jmax:
                jmax = j

for i in range(imin, imax+1, 1):
    for j in range(jmin, jmax+1, 1): # looping over minimum indicies, we print desired rectangle
        print(matrix[i][j], end="")
    print()

