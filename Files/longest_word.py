import os

dirname = input('Enter a directory name: ')

def longest_word(filename):
    return sorted(open(filename).read().split(), key=len, reverse=True)[0]

print({filename : longest_word(os.path.join(dirname, filename))
       for filename in os.listdir(dirname)
       if os.path.isfile(os.path.join(dirname, filename))})
