import math

n, d = input().split(" ")
moves = 0
numbers = input().split()

for i in range(int(n) - 1):  
    if(int(numbers[i+1]) <= int(numbers[i])): # if the number following is less than the current number
        diff = int(numbers[i]) - int(numbers[i+1]) # we need to first know by how much it is less
        numbers[i+1] = int(numbers[i+1]) + (math.ceil((diff + 1) / (int(d))) * int(d)) # we can then add d to our number diff times
        moves += math.ceil((diff + 1) / (int(d))) # add moves to how many times d was added to the number
            

print(moves)

