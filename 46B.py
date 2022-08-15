Sizes = ["S", "M", "L", "XL", "XXL"] # sizes list defined as constant

stock = list(map(int, input().split())) # get number of each size in stock and convert to int in list
costumers = int(input())
sold = []

for i in range(costumers): # loop over each costumer as they approach
    j = Sizes.index(input()) # index in stock list is the same index for given size as the Sizes list (for example if given "S", the index in both lists would be 0)
    k = j # k starts the same as j
    if stock[j] > 0: # if there is enough shirts in stock with this size, sell it and decrease the number in stock of this size
        sold.append(Sizes[j])
        stock[j] -= 1
    else: # if not, we need 2 variables to denote the movement left and right in our stock list, j->right, k->left
        while True: # k and j move by 1 each time
            k -= 1
            j += 1
            if j < len(stock) and stock[j] > 0: # as soon as we find the larger closest size in stock, we sell it
                sold.append(Sizes[j])
                stock[j] -= 1
                break
            elif k >= 0 and stock[k] > 0:# as soon as we find the smaller closest size in stock, we sell it
                sold.append(Sizes[k])
                stock[k] -= 1
                break
            
for item in sold:
    print(item)