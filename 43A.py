n = int(input())
goals = []
max = 0

for i in range(n):
    goals.append(input())

won = goals[0] # start by assuming the first team already won
for team in goals:
    curr_frequency = goals.count(team) # curr_freq denotes the number of occurances for team in our list
    if(curr_frequency > max): # if it is bigger then our maximum, then it is the current maximum
        max = curr_frequency
        won = team # this is the new winning team

print(won)