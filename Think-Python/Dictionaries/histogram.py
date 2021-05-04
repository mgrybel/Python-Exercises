def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


result1 = histogram('banana')
print(result1) # prints {'b': 1, 'a': 3, 'n': 2}
 