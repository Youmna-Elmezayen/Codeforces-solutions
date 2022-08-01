def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


ns, ks = input().split()
n, k = int(ns), int(ks)
neighbor = True
listOfPrimes = []
count = 0

for i in range(2, n+1):
    if isPrime(i):
        listOfPrimes.append(i) # create list of primes between 2 and n

for item in listOfPrimes: # loop over list of primes
    even = item - 1 # get the even number that is -1 of the current number (since we will add this 1 anyway to satisfy Noldbach condition)
    if even > 2: # if an even number is greater than 2, it can be written as the sum of 2 primes (Goldbach)
        for j in range(len(listOfPrimes)-1): 
            sum = listOfPrimes[j] + listOfPrimes[j+1] # check to see if 2 neighboring primes sum to our even number
            if sum == even:
                count += 1

if count == k or k == 0: # if k = 0, it is always true (at least)
    print("YES")
else:
    print("NO")