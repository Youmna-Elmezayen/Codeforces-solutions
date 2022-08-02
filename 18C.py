n = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in range(n-1): # n-1 because we add 1 to it when we reach the element before the last anyway
    piece1 = numbers[0:i+1] # slice list into piece1 that keeps increasing 
    piece2 = numbers[i+1:n] # slice list into piece2 that keeps decreasing 
    if sum(piece1) == sum(piece2): # if they have the same sum, increment count
        count += 1

print(count)