n, d = input().split()
ways = 0

heights = input().split()
heights = list(map(int, heights))

heights.sort()

for i in range(len(heights)-1):
    for j in range(i + 1, len(heights)):
        if heights[j] - heights[i] <= int(d):
            ways += 2
     
print(ways)