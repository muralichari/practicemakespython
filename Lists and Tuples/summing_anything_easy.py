def mysum(*inputlist):
    if not inputlist:
        return inputlist
    total = type(inputlist[0])()
    for i in inputlist:
        total += i
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



