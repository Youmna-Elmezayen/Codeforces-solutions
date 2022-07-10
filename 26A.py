from collections import Counter

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

n = int(input())
count = 0
dct = {}

for i in range(2, n+1):
    if not(isPrime(i)):
        for j in range(2, i+1):
            if i % j == 0:
                res = int(i / j)
                if isPrime(res):
                    if i in dct:
                        dct.update({i: dct[i] + 1})
                    else:
                        dct[i] = 1

for item in dct.values():
    if item == 2:
        count += 1

print(count)