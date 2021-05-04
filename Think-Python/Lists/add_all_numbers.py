def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


list1 = [1, 2, 3, 4]
result1 = add_all(list1)
print(result1) # prints 10

result2 = sum(list1) # built-in function sum
print(result2) # prints 10