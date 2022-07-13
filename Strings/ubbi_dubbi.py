to_convert = input('Please enter a word to convert to Ubbi Dubbi: ')

result = ''
for i in to_convert:
    if i in 'aeiou':
        result = result + 'ub' + i
    else:
        result =  result + i
print(result)