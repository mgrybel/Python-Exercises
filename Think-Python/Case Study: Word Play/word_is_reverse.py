def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)-1

    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    
    return True


result1 = is_reverse(word1='banana', word2='banana')
print(result1) # prints False

result2 = is_reverse(word1='banana', word2='ananab')
print(result2) # prints True