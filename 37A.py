from math import ceil

n = int(input())
towers = 0
height = 1
max_height = 1

sizes = input().split()
sizes = list(map(int, sizes))
sizes.sort() # sort to keep duplicates next to each other

for i in range(n):
    if(i == n - 1): # if the selected element is last element, we cannot access +1 index which means it will have to add 1 to towers
        towers += 1
    else:
        if not (sizes[i] == sizes[i+1]):# if elements are not equal, they all denote different towers
            towers += 1
            height = 1 # height of tower starts at 1
        else: # if elements are equal, then we add the height and if it is greater than max, we set it to max. We do not need to add towers until we reach final duplicate
            height += 1
            if height >= max_height:
                max_height = height
    
print(str(max_height) + " " + str(towers))

