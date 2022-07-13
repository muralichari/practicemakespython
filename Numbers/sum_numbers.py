def mysum(*inputnumbers):
        total = 0
        for i in inputnumbers:
                total += i
        return total

totalsum1 = mysum(1,2,4)
print(f'Total sum for individual numbers is {totalsum1}')

totalsum2 = mysum(*[4,5,6])
print(f'Total sum for list is {totalsum2}')
