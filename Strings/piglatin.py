to_convert = input('Please enter a string to convert to Pig Latin: ')

result = ''
if str(to_convert[0]) in ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    result = to_convert + 'way'
else:
    result = to_convert[1:] + to_convert[0] + 'ay'
print(result)