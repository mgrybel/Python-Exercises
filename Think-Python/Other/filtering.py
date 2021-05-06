def only_upper_v1(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


# using list comprehension
def only_upper_v2(t):
    return [s for s in t if s.isupper()]


result1 = only_upper_v1('Hello, World!')
print(result1)

result2 = only_upper_v2('Hello, World!')
print(result2)