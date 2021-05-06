def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


result = has_no_e('Python')
print(result) # prints True
