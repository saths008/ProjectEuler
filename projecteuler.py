#multiples of 3 and 5
numbers = list(range(1,1000))
newList = []
for x in numbers:  #if remainder equals 0, it is divisible
    if x % 5 == 0:
        newList.append(x)
    if x % 3 == 0:
        newList.append(x)

print(newList)

finalmutliplierlist = list(dict.fromkeys(newList))

print(finalmutliplierlist)

print(sum(finalmutliplierlist))
