sourceStr = input()
destinationStr = input()
directions = []

source = [sourceStr[0], sourceStr[1]]
destination = [destinationStr[0], destinationStr[1]]

while not source == destination:
    if(source[0] < destination[0] and source[1] > destination[1]):
        source[0] = chr(ord(source[0]) + 1)
        source[1] = chr(ord(source[1]) - 1)
        directions.append('RD')
    elif(source[0] > destination[0] and source[1] > destination[1]):
        source[0] = chr(ord(source[0]) - 1)
        source[1] = chr(ord(source[1]) - 1)
        directions.append('LD')
    elif(source[0] < destination[0] and source[1] < destination[1]):
        source[0] = chr(ord(source[0]) + 1)
        source[1] = chr(ord(source[1]) + 1)
        directions.append('RU')
    elif(source[0] > destination[0] and source[1] < destination[1]):
        source[0] = chr(ord(source[0]) - 1)
        source[1] = chr(ord(source[1]) + 1)
        directions.append('LU')

    if(source[0] < destination[0] and source[1] == destination[1]):
        source[0] = chr(ord(source[0]) + 1)
        directions.append('R')
    elif(source[0] > destination[0] and source[1] == destination[1]):
        source[0] = chr(ord(source[0]) - 1)
        directions.append('L')

    if(source[0] == destination[0] and source[1] < destination[1]):
        source[1] = chr(ord(source[1]) + 1)
        directions.append('U')
    elif(source[0] == destination[0] and source[1] > destination[1]):
        source[1] = chr(ord(source[1]) - 1)
        directions.append('D')

print(len(directions))
for dir in directions:
    print(dir)
