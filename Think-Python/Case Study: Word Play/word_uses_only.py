def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


result = uses_only(word='Python', available='y')
print(result) # prints False

result2 = uses_only(word='Python', available='Python')
print(result2) # prints True
