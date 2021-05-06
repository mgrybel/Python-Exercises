def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)


res = avoids('Python', 'y')
print(res) # prints False

res2 = avoids('Python', 'Y')
print(res2) # prints True

res3 = avoids('Python', 'm')
print(res3) # prints True