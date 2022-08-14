heading = input()
text = input()

text = text.replace(" ", "") # Empty out the spaces, they will not be counted
heading = heading.replace(" ", "")

for i in range(len(text)):
    if not text[i] in heading or (text.count(text[i]) > heading.count(text[i])): # if the character we need does not exist in the heading or if we need it more than the times it exists
        print("NO") # we cannot create text from heading
        break

else: # else, we can
    print("YES")