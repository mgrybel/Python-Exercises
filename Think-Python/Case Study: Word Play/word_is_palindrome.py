from word_is_reverse import is_reverse

def is_palindrome(word):
    i = 0
    j = len(word)-1

    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True


def is_palindrome_v2(word):
    return is_reverse(word, word)


result1 = is_palindrome(word='level')
print('is level a palindrome? ' + str(result1)) # True

result2 = is_palindrome(word='Level')
print('is Level a palindrome? ' + str(result2)) # False

result3 = is_palindrome_v2('level')
print('is level a palindrome? ' + str(result3)) # True

result4 = is_palindrome_v2('Level')
print('is Level a palindrome? ' + str(result4)) # False

result5 = is_palindrome('radar')
print('is radar a palindrome? ' + str(result5)) # True

result6 = is_palindrome_v2('banana')
print('is banana a palindrome? ' + str(result6)) # False