ns, ms = input().split()
n, m = int(ns), int(ms)
prices = list(map(int, input().split()))
prices.sort()

fruits = {} # dictionary to carry fruits and number of occurances
a, b = 0, 0
for i in range(m):
    fruit = input()
    if fruit in fruits: # if element already exists just update its value
        fruits[fruit] += 1
    else: # if element doesn't exist add it with value 1
        fruits[fruit] = 1

sorted_fruits = {key: val for key, val in sorted(fruits.items(), key = lambda ele: ele[1], reverse=True)} # sort dict wrt values(count)

i = 0 # index for least prices (from beginning of prices list)
j = len(prices) - 1 # index for most prices (from end of prices list)
for value, key in sorted_fruits.items():
   a += (key * prices[i]) # multiply key by least price and add together to get minimum cost
   i += 1
   b += (key * prices[j]) # multiply key by most price and add together to get maximum cost
   j -= 1

print(str(a) + " " + str(b))