COORDINATE_COUNT = 3

fly1 = input().replace(" ", "") # remove spaces to just deal with characters
fly2 = input().replace(" ", "")
count = 0

for i in range(COORDINATE_COUNT):
    if not(fly1[i] == fly2[i]): #  count how many different coordinates are there
        count += 1

if count <= 2: # if different coordinates is 2 or less, they both exist on the same face
    print("YES")
else:
    print("NO")