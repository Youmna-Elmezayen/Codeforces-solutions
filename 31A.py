n = int(input())
lengths = list(map(int, input().split()))
index = [-1]

for i in range(n): # loop over all elements to add to one another
    for j in range(i+1, n):
        sum = lengths[i] + lengths[j]
        if sum in lengths: # if sum is in our list
            if -1 in index:
                index.remove(-1) # remove -1 from inital index list
            index.append(lengths.index(sum)+1) # append the index (1 based not 0) of the sum
            index.append(i+1) # append the index (1 based not 0) of the first element
            index.append(j+1) # append the index (1 based not 0) of the second element
        
if len(index) > 2: # if sum(s) were found, print any of them (1st set)      
    print(str(index[0]) + " " + str(index[1]) + " " + str(index[2]))
else: # if none is found, print the only value in index which is -1
    print(index[0])