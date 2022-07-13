mylist = list(range(0,10))
alias = mylist

mylist[:] = ['a'] * 6

print(mylist)
print(alias)
