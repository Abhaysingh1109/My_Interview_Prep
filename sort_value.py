my_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 2}

valueSorted = dict(sorted(my_dict.items(), key = lambda item: item[1]))
print(valueSorted)