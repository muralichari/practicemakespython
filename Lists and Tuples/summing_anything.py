def mysum(*inputlist):
    if isinstance(inputlist[0], int):
        total = 0
        for i in inputlist:
            total += i
        return total
    elif isinstance(inputlist[0], str):
        total = ""
        for i in inputlist:
            total = total + i
        return total

    elif isinstance(inputlist[0], list):
        total = []
        for i in inputlist:
            total.append(i)
        return total

    elif isinstance(inputlist[0], tuple):
        total = []
        for i in inputlist:
            total.append(i)
        return total


totalsum1 = mysum(1,2,3)
print(f'Total sum for individual numbers is {totalsum1}')

totalsum2 = mysum(*[4, 5, 6])
print(f'Total sum for list of numbers is {totalsum2}')


totalsum2 = mysum('a', 'b', 'c')
print(f'Total sum for characters is {totalsum2}')

totalsum2 = mysum(['a', 'b', 'c'], [1,2,3])
print(f'Total sum for list is {totalsum2}')

totalsum2 = mysum(('a', 'b', 'c'), (1,2,3))
print(f'Total sum for tuple is {totalsum2}')



