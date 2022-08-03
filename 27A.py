n = int(input())
tasks = list(map(int, input().split()))
index = -1

for i in range(1, 3001): # make a loop that goes through all possible task indices 
    if not (i in tasks): #the first small number it encounters that doesn't already exists is the answer
        index = i
        break

if index == -1: # if all the indices are after another, the min is 1 + the greatest index 
    tasks.sort()
    index = tasks[n-1] + 1

print(index)