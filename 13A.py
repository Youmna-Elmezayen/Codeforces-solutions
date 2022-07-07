import math
from fractions import Fraction

a = int(input())
bases = []

for j in range(2, a, 1):
    if a < j: # if number is less than base, it is the same as it is 
        bases.append(a)
    else:
        copy = a
        while not (copy == 0):
            bases.append(copy % j) # append remainder of division to the bases list
            copy = math.floor(copy / j) # keep dividing until reaching 0

average = Fraction(sum(bases) / (a - 2)).limit_denominator() 
if(str(average).isdigit()):# if average is a whole number, add "/1" manually to it
    print(str(average) + "/1")
else:
    print(average)