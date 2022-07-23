dS, sumTimeS = input().split()
d, sumTime = int(dS), int(sumTimeS)
maxTime, minTime = [], []

for i in range(d):
    interval = input().split()
    minTime.append(int(interval[0])) # list of minimum times
    maxTime.append(int(interval[1])) # list of maximum times

sumMaxTime = sum(maxTime) # sum all max times
sumMinTime = sum(minTime) # sum all min times

if sumMinTime <= sumTime <= sumMaxTime: # if sumTime is within total interval, then we can divide it into the days
    print("YES")
    for i in range(d):
        t = min(minTime[i] + sumTime - sumMinTime, maxTime[i]) # time is the least I can get from interval and still have sumTime left for next day(s)
        print(t, end=" ")
        sumTime -= (t - minTime[i]) # subtract sumTime from t and keep going through all days
else:
    print("NO")
