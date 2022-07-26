n = input()
m = input()

digits = list(tuple(map(str, n))) # tuple to take every digit in our number in and turn tuple into list to sort
digits.sort()

if digits[0] == '0' and len(digits) > 1: # swap 0 with 2nd smallest element
    digits[0], digits[1] = digits[1], digits[0]

correct_answer = ""
for i in range(len(digits)):
    correct_answer += digits[i] # concat digits to get correct answer

if correct_answer == m: # compare concat string with bob's answer m
    print("OK")
else: 
    print("WRONG_ANSWER")