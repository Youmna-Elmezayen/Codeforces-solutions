n = int(input())
camel = []
flag = False

for i in range(n):
    camel.append(input().split())
    camel[i][0] = int(camel[i][0]) 
    camel[i][1] = int(camel[i][1])


for i in range(len(camel)):
    sum = camel[i][0] + camel[i][1] # get sum of x and d
    for j in range(i + 1, len(camel)):
        if sum == camel[j][0]: # is sum is equal to position of another camel
            sum2 = camel[j][0] + camel[j][1] # check to see if this other camel also spit on the first (selected) camel
            if sum2 == camel[i][0]:
                flag = True # flag is set to true if both camels spit on each other
                break
    if flag:
        print("YES")
        break

if not flag:
    print("NO")