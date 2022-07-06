from fractions import Fraction

y, w = input().split(" ")
max = max(int(y), int(w))
count = 0

for i in range(max, 7, 1): # get how many numbers can be rolled and have Dot be the greatest(including max)
    count += 1

if(count == 6):
    print("1/1")
else:
    print(Fraction(count, 6).limit_denominator()) # divide number possible by 6 to get float then turn to fraction