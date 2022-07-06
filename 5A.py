bytesInMessages = 0
users = 0
totalBytes = 0

while True: # keep taking in input
    try:
        line = input()
        if not (line[0] == '+' or line[0] == '-'): # if command doesn't start with + or -, then it is a send command
            bytesInMessages = len(line.split(':')[1]) # get length of message and set it to bytes in message
            totalBytes += bytesInMessages * users # multiply bytes to number of users currently in chat to get total bytes trafficed
        elif(line[0] == '+'): # if command starts with +, increment users
            users += 1
        else:# if command starts with -, decrement users
            users -= 1
    except EOFError: # stop taking input when ctrl -D or ctrl -Z is encountered which indicates end of stream
        print(totalBytes) # print the total bytes when all commands are done 
        break
    
    

