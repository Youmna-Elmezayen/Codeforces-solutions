s  = input()
count = 0
search_word = "hello"

i = 0
for c in s:
    if c == search_word[i]: # we want exactly 5 characters that form hello, if we find one of them, we look for the next
        count += 1 
        i += 1 # index of hello is incremented

    if count == 5:
        print("YES")
        break

else:
    print("NO")
