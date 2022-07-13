filename = input("Enter a filename: ")
print(open(filename).readlines()[-1])