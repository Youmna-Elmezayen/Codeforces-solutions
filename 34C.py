with open('input.txt', 'r') as in_file: # open input file and read n and the sequence of 1s and 0s
    n = in_file.readline().strip() 
    sequence = in_file.readline().strip()
in_file.close()
subs = sequence.split("1") # split at the 1s to see if the patterns in between are equal

subs.remove(subs[0]) # remove first split because it is the first message so there is no pattern yet

for i in range(len(subs)-2): # ignore last element because it is the last message so nothing after matters
    if not subs[i] == subs[i+1]: # if encountered 2 not equal patterns
        with open('output.txt', 'w') as out_file: # write no to output file
            out_file.write("NO")
        break
else: # if all patterns are equal
    with open('output.txt', 'w') as out_file:# write yes to output file
        out_file.write("YES")

out_file.close()