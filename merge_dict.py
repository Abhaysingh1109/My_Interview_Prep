def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print(merge_dicts(d1, d2))