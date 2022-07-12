n = int(input())
years = list(map(int,input().split())) # convert years from list of strings to list of ints
current, next = input().split()

sum = 0

for i in range(int(current)-1, int(next)-1): # Current level denotes the need for which elements and next denotes up to what element in years
    sum += years[i]

print(sum)