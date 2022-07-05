import math

n, m, a = input().split()
n = int(n)
m = int(m)
a = int(a)

rowW = math.ceil(n / a)
columnW = math.ceil(m / a) 
print(rowW * columnW)