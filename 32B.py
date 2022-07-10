borze = input()
characters = []

i = 0
while i < len(borze):
    if borze[i] == ".": # if character is a dot, then what follows is not part of the digit
        characters.append(borze[i])
        i += 1 # add i by 1 because we only took one character
    else:
        characters.append(str(borze[i] + borze[i+1])) # if character is a dash, then what follows is a part of the digit so take 2 characters
        i += 2 # add i by 2 because we took two character


for token in characters:
    if token == "-.":
        print("1", end="")
    elif token == "--":
        print("2", end="")
    else:
        print("0", end="")

