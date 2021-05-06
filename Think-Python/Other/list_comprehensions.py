def capitalize_all_v1(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


# using list comprehension
def capitalize_avv_v2(t):
    return [s.capitalize() for s in t]


result1 = capitalize_all_v1('Hello, World!')
print(result1)

result2 = capitalize_avv_v2('Hello, World!')
print(result2)