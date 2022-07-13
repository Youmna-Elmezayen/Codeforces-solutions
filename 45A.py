import enum

class Month(enum.Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


current_month = input()
remain = int(input())

sum = Month[current_month].value + remain
if sum > 12: # if sum is greater than 12, we need to circle back to the start
    difference = sum - 12 # we get difference and keep subtracting it from 12 if it is still above until we get the desired number of month within 12
    while difference > 12:
        difference = difference - 12
        
    print(Month(difference).name)
else: # if sum is less than or equal 12, we can just print the month name right away
    print(Month(sum).name)