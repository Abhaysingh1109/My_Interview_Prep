def most_frequent(lst):
    return max(set(lst), key=lst.count)

numbers = [1, 2, 3, 2, 4, 2, 5, 3]

print(most_frequent(numbers))