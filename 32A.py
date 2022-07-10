n, d = input().split()
ways = 0

heights = input().split()
heights = list(map(int, heights)) # convert input string list to int list

heights.sort()

for i in range(len(heights)-1): # go over every entry and check it with every entry following it and check difference if less than or equal d
    for j in range(i + 1, len(heights)):
        if heights[j] - heights[i] <= int(d):
            ways += 2 # if difference is less than or equal d, then this accounts for 2 ways that these soldiers can be selected
     
print(ways)