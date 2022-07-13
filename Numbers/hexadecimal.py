
''' This program takes a hexadecimal number as input and prints out the decimal equivalent '''

hexinput = input('Please enter a hexadecimal string, e.g. 1F22: ')

decnumber = 0
for i, j in enumerate(reversed(hexinput)):
  decnumber += int(j,16) * (16 ** i)

print(f'The decimal equivalent is {decnumber}')
