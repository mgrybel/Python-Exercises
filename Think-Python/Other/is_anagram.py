from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)


result = is_anagram('listen', 'silent')
print(result) # prints True

result2 = is_anagram('monty', 'python')
print(result2) # prints False
