n = int(input())
digits = list(tuple(map(str, input()))) # tuple to take every digit in our number in and turn tuple into list 
answer = ""

if n % 2 == 0: # if n is divisible by 2, we just divide it into groups of 2
    i = 0
    while i < n - 1:
        answer += (digits[i] + digits[i+1])
        i += 2
        if i < n - 1: # add dash only if there is another group of 2 coming
            answer += "-"
elif n % 3 == 0: # if n is divisible by 3, we just divide it into groups of 3
    i = 0
    while i < n - 2:
        answer += (digits[i] + digits[i+1] + digits[i+2])
        i += 3
        if i < n - 2: # add dash only if there is another group of 3 coming
            answer += "-"
else:
    answer = (digits[0] + digits[1] + digits[2] + "-") # if it is neither, we can first take a group of 3 and thus making the len of rest divisible by 2 and placed as groups of 2
    i = 3 # start at the 4th element
    while i < n - 1:
        answer += (digits[i] + digits[i+1])
        i += 2
        if i < n - 1: # add dash only if there is another group of 2 coming
            answer += "-"

print(answer)