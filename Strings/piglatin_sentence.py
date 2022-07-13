to_convert = input('Please enter a sentence to convert to Pig Latin: ')

result = ""
output = []
for word in to_convert.split():
    if str(word[0]) in ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        result = word + 'way'
    else:
        result = word[1:] + word[0] + 'ay'
    output.append(result)
print(' '.join(output))