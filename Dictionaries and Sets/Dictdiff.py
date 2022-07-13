def dictdiff(d1, d2):
    output = {}
    all_keys = set(d1.keys())
    all_keys.update(d2.keys())

    for key in all_keys:
        if d1.get(key) != d2.get(key):
            output[key] = [d1.get(key), d2.get(key)]
    print(all_keys)
    return output


d1 = {'a':1, 'b':4, 'c':3}
d2 = {'a':1, 'b':2, 'd':4}


print(dictdiff(d1,d2))