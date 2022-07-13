from math import sqrt

n = int(input())
test = sqrt((8 * n) + 1) # the rule that every triangular number follows (from Wikipedia)

if float.is_integer(test):
    print("YES")
else:
    print("NO")