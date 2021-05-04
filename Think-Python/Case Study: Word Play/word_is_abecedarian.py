def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


# using recursion
def is_abecedarian_v2(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_v2(word[1:])


# using a while loop
def is_abecedarian_v3(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i + 1
    return True


result1 = is_abecedarian(word='abcdef')
print(result1) # prints True

result2 = is_abecedarian(word='zzzabczzz')
print(result2) # prints False

result3 = is_abecedarian_v2(word='abcdef')
print(result3) # prints True

result4 = is_abecedarian_v2(word='zzzabczzz')
print(result4) # prints False

result5 = is_abecedarian_v3(word='abcdef')
print(result5) # prints True

result6 = is_abecedarian_v3(word='zzzabczzz')
print(result6) # prints False