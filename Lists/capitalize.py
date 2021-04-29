def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

list1 = ['a', 'b', 'c', 'd']
result = capitalize_all(list1)
print(result) # prints ['A', 'B', 'C', 'D']
