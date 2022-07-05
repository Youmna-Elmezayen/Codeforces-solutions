w = int(input())

if w % 2 != 0 or w == 2: #if w is odd, it cannot be divided into odd weighing pieces. 
    print("NO")
else: #if w is even, it can always be divided into even weighing pieces.8
    print("YES")
