with open('input.txt', 'r') as f: # read from file
    lines = f.readlines()

original = lines[0].strip() # first line is original position of ball
for i in range(1, len(lines)):
    shuffle = lines[i].strip().split()
    if shuffle[0] == original: # if the first shuffled index is equal to the original, then the new original is the other index
        original = shuffle[1]
    elif shuffle[1] == original:
        original = shuffle[0]

file1 = open('output.txt', 'w')# write to file
file1.writelines(original)
file1.close()