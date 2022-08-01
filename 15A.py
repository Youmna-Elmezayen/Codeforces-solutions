ns, ts = input().split()
n, t = int(ns), int(ts)
orientations = 2 # always starts with 2 (1 left to the very first house and 1 right to the very last house)
flag = False

houses = []
for i in range(n):
    houses.append(list(map(int, input().split())))

houses.sort() # sort (default) by first element in sublists which is the center point

for i in range(n):
    distanceLeft = houses[i][0] - ((houses[i][1] / 2) + t) # we get the distance available left to the current house by subtracting the distance from the center of the current house added to the distance of the new house
    if i > 0 and distanceLeft > houses[i-1][0] + (houses[i-1][1] / 2): # if the distance is enough between this house and the prev one
        orientations += 1
    elif i > 0 and distanceLeft == houses[i-1][0] + (houses[i-1][1] / 2): # if the distance is exactly equal, we need to count this orientation only once
        if not flag:
            orientations += 1
        else:
            flag = False
    distanceRight = houses[i][0] + ((houses[i][1] / 2) + t) # we get the distance available left to the current house by adding the distance from the center of the current house added to the distance of the new house
    if i < n-1 and distanceRight < houses[i+1][0] - (houses[i+1][1] / 2): # if the distance is enough between this house and the next one
        orientations += 1
    elif i < n-1 and distanceRight == houses[i+1][0] - (houses[i+1][1] / 2): # if the distance is exactly equal, we need to count this orientation only once
        if not flag:
            orientations += 1
            flag = True
        else:
            flag = False

print(orientations)