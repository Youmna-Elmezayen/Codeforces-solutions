n = int(input())

sequence = input().split()
count = 0

if sequence.count("1") >= sequence.count("2") and sequence.count("1") >= sequence.count("3"): # if the most repeated # is 1 then the rest will hbe changed to 1
    count += (sequence.count("2") + sequence.count("3"))
elif sequence.count("2") >= sequence.count("1") and sequence.count("2") >= sequence.count("3"): # if the most repeated # is 2 then the rest will hbe changed to 2
    count += (sequence.count("1") + sequence.count("3"))
elif sequence.count("3") >= sequence.count("1") and sequence.count("3") >= sequence.count("2"): # if the most repeated # is 3 then the rest will hbe changed to 3
    count += (sequence.count("1") + sequence.count("2"))

print(count)
