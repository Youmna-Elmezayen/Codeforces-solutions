coins = {"A": 0, "B": 0, "C": 0} # dictionary to hold coins and number of how many times each were seen as minmums to each other

for i in range(3):
    comparison = input()
    if comparison[1] == '>':
        coins[comparison[2]] += 1 # in case of comp[0] > comp[2], comp[2] is minimum so its count goes up
    else:# in case of comp[0] < comp[2], comp[0] is minimum so its count goes up
        coins[comparison[0]] += 1

sorted = dict(sorted(coins.items(), key=lambda item:item[1], reverse=True)) # sort in reverse the keys (counts)
unique = set(sorted.values()) # try to get rid of duplicates. Duplicates will only happen if it is impossible to get these comparisons
if len(unique) == 3: # if there are 3 unique counts, it is possible
    for key in sorted.keys():
        print(key, end="")
else:
    print("Impossible")
    