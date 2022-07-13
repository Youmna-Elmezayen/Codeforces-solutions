n = int(input())
counter = 1
children = [i for i in range(1,n+1)] # list of children postitions from 1 to n
received = [] # initialized empty list to carry the positions of children who recieved the ball

i = 0
while len(received) < (n-1): # because only n - 1 are supposed to recieve the ball before the game ends
        i += counter # counter is used as the steps between children with every throw
        if i > (n-1): # if we reach the end, we need to circle back to the start 
            diff = abs(n - i) # difference will take us back to desired position
            i = diff
            received.append(children[i])
        else:
            received.append(children[i])
        counter += 1 # increment step by 1 every time

for item in received:
    print(item, end=" ")
