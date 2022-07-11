n = int(input())
index1, index2 = 0, 0
min = 1000

heights = input().split()
heights = list(map(int, heights)) # convert input string list to int list


for i in range(n):
    if i == n-1: # in case the selected element is the last element in the list and we cannot index +1, +1 will be element[0]
        if abs(heights[i] - heights[0]) <= min: # if difference in height is less than minimum, then this is the new minimum
            min = abs(heights[i] - heights[0])
            index1, index2 = i, 0 # save indices of minimum heights
        elif abs(heights[i] - heights[i-1]) <= min:
            min = abs(heights[i] - heights[i-1])
            index1, index2 = i-1, i
    else:
        if abs(heights[i] - heights[i+1]) <= min:
            min = abs(heights[i] - heights[i+1])
            index1, index2 = i, i+1
        elif abs(heights[i] - heights[i-1]) <= min:
            min = abs(heights[i] - heights[i-1])
            index1, index2 = i-1, i

print(str(index1 + 1) + " " + str(index2 + 1))