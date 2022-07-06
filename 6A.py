import math

a, b, c, d = input().split(" ")

list = [int(a), int(b) ,int(c) ,int(d)]
list.sort() # sort list of inputs ascendingly

#taking any 3 of our list together, each 2 sides have to add up to more than the 3rd side
if(list[0] + list[1] > list[2] or list[1] + list[2] > list[3] or list[0] + list[1] > list[3] or list[0] + list[2] > list[3]):
    print("TRIANGLE")
#if the sum is equal to 3rd side, then it is a degenerate triangle
elif(list[0] + list[1] == list[2] or list[1] + list[2] == list[3] or list[0] + list[1] == list[3] or list[0] + list[2] == list[3]):
    print("SEGMENT")
else: # else it is impossible to create a triangle
    print("IMPOSSIBLE")