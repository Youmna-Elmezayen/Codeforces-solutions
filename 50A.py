import math

ms, ns = input().split()
m, n = int(ms), int(ns)

print(math.floor((m * n) / 2)) # floor because we don't want to get over the border