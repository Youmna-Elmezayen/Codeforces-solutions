n, x0 = input().split(" ")
startMax, endMin = 0, 1000

for i in range(int(n)):
    segment = input().split(" ")
    segment[0], segment[1] = int(segment[0]), int(segment[1])
    segment.sort() # sort incoming range
    if segment[0] >= startMax: # we get the maximum start for our ranges
        startMax = segment[0]
    if segment[1] <= endMin:# we get the minimum end for our ranges
        endMin = segment[1]

if startMax > endMin: # if range is incorrect ie: the start is not less than the end
    print("-1")
elif (startMax <= int(x0) and int(x0) <= endMin): # if the inital position is already within our range
    print("0")
else:
    print(min(abs(int(x0) - startMax), abs(int(x0) - endMin)))