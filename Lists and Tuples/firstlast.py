
def firstlast(sequence):
    return sequence[:1] + sequence[-1:]

# return a list
to_be_clipped = 'hello'

print("Clipped list")
print (firstlast(to_be_clipped))

# return a tuple
print("Clipped tuple")
to_be_clipped = ('a', 'b', 'c')
print (firstlast(to_be_clipped))

# return a numeric tuple
print("Clipped list")
to_be_clipped = [1,2,3]
print (firstlast(to_be_clipped))
