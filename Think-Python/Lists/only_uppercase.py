def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


list1 = ['A', 'b', 'C', 'd', 'E']
result = only_upper(list1)
print(result) # prints ['A', 'C', 'E']
