n = int(input())
nSet = set()

in_list = input().split()
for entry in in_list:
    entry = int(entry)
    nSet.add(entry)

in_list = list(nSet)
in_list.sort()

if len(in_list) >= 2:
    print(in_list[1])
else:
    print("NO")