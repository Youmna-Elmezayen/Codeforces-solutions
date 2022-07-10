n = int(input())
nSet = set() # a set will help get rid of duplicates

in_list = input().split()
for entry in in_list:
    entry = int(entry)
    nSet.add(entry) # only unique entries will be added

in_list = list(nSet)
in_list.sort() # sort list with no duplicates

if len(in_list) >= 2: # if second order exists print it
    print(in_list[1])
else:
    print("NO")