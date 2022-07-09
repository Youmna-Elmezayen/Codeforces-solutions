n, m = input().split(" ")
rows = []
flag = True

for i in range(int(n)):
    row = input().strip(" ")
    rows.append(row)
    for j in range(int(m) - 1): # first false case is a single row doesn't have all equivalent elements
        if not(row[j] == row[j+1]):
            flag = False

for i in range(int(n) - 1): # second false case is adjacent rows having the same elements
    if rows[i] == rows[i+1]:
        flag = False

if flag:
    print("YES")
else:
    print("NO")