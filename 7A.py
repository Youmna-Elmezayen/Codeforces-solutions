NumberOfRows = 8 # constant for row size
FullRow = "BBBBBBBB" # constant for a complete black row

count = 0

for i in range(NumberOfRows):
    row = input()
    if row == FullRow: # if current row is to be black
        count += 1 # we need 1 horizontal stroke to color it
    else:
        notFullRow = row # the not full row will tell us what columns need vertical strokes(how many)

if not (count == NumberOfRows):
    for c in notFullRow: # check black columns in not full row
        if c == 'B':
            count += 1

print(count)