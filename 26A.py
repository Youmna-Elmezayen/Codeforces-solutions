from collections import Counter

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0: # definition of prime is that the number only has 1 and itself as factors
                return False
        return True

n = int(input())
count = 0
dct = {}

for i in range(2, n+1): # for numbers within 2 and n inclusive(n+1)
    if not(isPrime(i)): # if current number is prime, this means that it doesn't have any factors that can be prime
        for j in range(2, i+1): # divide by all numbers that are less than or equal to current number
            if i % j == 0:
                res = int(i / j)
                if isPrime(res): # if result is prime, add i to dictionary as key and number of prime factors as value
                    if i in dct:
                        dct.update({i: dct[i] + 1}) # increment value(occurances) if key already exists in dictionary
                    else:
                        dct[i] = 1

for item in dct.values(): # for all entries in dictionary, if the number of prime factors = 2 then this is included in count
    if item == 2:
        count += 1

print(count)