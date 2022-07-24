import fnmatch

stations = input()
firstSight = input()
secondSight = input()

strCheck = "*" + firstSight + "*" + secondSight + "*" # using wild cards, we need to know if these sights are seen in the correct order
forward = fnmatch.fnmatch(stations, strCheck) #fnmatch checks if a string with this pattern exists in stations

stationsReverse = stations[::-1] # reverse stations
backward = fnmatch.fnmatch(stationsReverse, strCheck) # backward will have the same strCheck but with reversed stations string

if forward and backward:
    print("both")
elif forward and not backward:
    print("forward")
elif backward and not forward:
    print("backward")
else:
    print("fantasy")