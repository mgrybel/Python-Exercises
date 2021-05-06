def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


result = uses_all(word='Python', required='y')
print(result) # prints True

result2 = uses_all(word='Python', required='yon')
print(result2) # prints True

result3 = uses_all(word='Python', required='abcdef')
print(result3) # prints False