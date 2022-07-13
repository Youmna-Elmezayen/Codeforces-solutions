n = int(input())
leaves = []
count = 0

for i in range(n):
    leaves.append(input())

leaves.sort() # sorting will place all similar elements next to each other

for i in range(len(leaves)):
    if i == len(leaves) - 1: # if we are at the last element, it will be counted either way whether it was a duplicate(last duplicate) or unique
        count += 1
    else:
        if not (leaves[i] == leaves[i+1]): # count the unique leaves only that is picked up (or last duplicates)
            count += 1

print(count)