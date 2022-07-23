n = int(input())
speeds = list(map(int, input().split()))
bobCount, aliceCount = 0, 0

i = 0 # pointer to alice
j = n - 1 # pointer to bob
alice = speeds[i] # current piece alice is eating
bob = speeds[j] # current piece bob is eating

if n == 1: # list has only 1, alice will eat it
    aliceCount += 1
else:
    while i <= j: # if i is still within j, the pieces are not done
        if alice <= bob: # if alice has less sum of time left to finish piece (or equal since bob is a gentleman)
            i += 1
            alice += speeds[i] # prefix sum of alice pieces
            aliceCount += 1 # alice finishes another piece
        else:
            j -= 1
            bob += speeds[j] # prefix sum of bob pieces
            bobCount += 1 # bob finishes another piece



print(str(aliceCount) + " " + str(bobCount))