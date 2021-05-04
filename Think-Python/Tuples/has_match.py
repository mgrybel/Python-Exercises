def has_match(t1, t2):
    for x,y in zip(t1, t2):
        if x == y:
            return True
    return False


t1 = ('a', 'b', 'c', 1, 2, 3)
t2 = ('d', 'e', 'f')
t3 = ('a', 'b', 'c', 1, 2, 3)

print(type(t1)) # tuple
print(type(t2)) # tuple
print(type(t3)) # tuple

result1 = has_match(t1, t2)
result2 = has_match(t1, t3)

print(result1) # prints False
print(result2) # prints True