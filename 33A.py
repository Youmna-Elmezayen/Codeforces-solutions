rows = {} # dictionary to hold rows and each their viability
count = 0

n, m, k = map(int, input().split())

for i in range(m):
    rows[i] = 1000000 # initialize dictionary by the max viability

for i in range(n):
    r, c = map(int, input().split())
    if rows[r-1] >= c: # viability of a row is the viability of the least viable tooth in that row so we get minimum for row
        rows[r-1] = c
    
for value in rows.values(): # add viabilites for all rows
    count += value

print(min(count, k)) # if the portion is less than count, then it can eat the whole portion