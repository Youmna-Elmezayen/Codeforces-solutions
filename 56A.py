def isAlcohol(answer):
    if answer in ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]:
        return True
    return False

n = int(input())
checked = 0

for i in range(n):
    answer = input()
    if isAlcohol(answer): # first case to check is if the drink ordered is alcoholic
        checked += 1
    elif answer.isnumeric() and int(answer) < 18: # second case to check is if the age given is less than 18
        checked += 1

print(checked)