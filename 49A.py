def isVowel(character):
    if character.lower() in ('a', 'e', 'i', 'o', 'u', 'y'):
        return True

question = input().split()
n = len(question)

last_token = question[n - 1]
if last_token == "?": # if the last seperated token is a question mark, then the word right before it is the one we want
    last_word = question[n - 2]
else:
    last_word = last_token[0:len(last_token) - 1:1] # if the quesiton mark is part of the last token, the last word is one character less

m = len(last_word)
if isVowel(last_word[m - 1]):# check last character of last word is vowel or not
    print("YES")
else:
    print("NO")