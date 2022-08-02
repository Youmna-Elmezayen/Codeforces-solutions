string = input()
substrings = {} # dict to hold substrings and number of occurances
max = 0

for i in range(len(string)): # i keeps track of the start of the current substring
    j = 0
    while j < (len(string)): # j keeps track of the end of the current substring
        substring = string[i:j+1]
        if substring in substrings.keys(): # if substring exists in our dict, add its counter by 1
            substrings[substring] += 1
        else: # if substring doesn't exist in our dict, place it in and set counter to 1
            substrings[substring] = 1
        j += 1

for substring in substrings.keys(): # loop over dictionary keys(substrings)
    if substrings[substring] >= 2 and len(substring) > max: # see if the counter is greater than or equal to 2 and the max length is the greatest
        max = len(substring)

print(max)