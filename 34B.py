n, m = input().split()
intM = int(m)
negatives = []
sumMoney = 0

inp = input().split()
inp = list(map(int, inp))
for i in range(int(n)):
    if inp[i] < 0:
        negatives.append(inp[i]) # create a list with only negative numbers(possible earnings)

negatives.sort()

for i in range(len(negatives)):
    if intM > 0: # intM is the amount of TVs he can carry
        sumMoney += abs(negatives[i]) # his earnings is added to the next negative value as long as he can still carry more TVs
        intM -= 1

print(sumMoney)