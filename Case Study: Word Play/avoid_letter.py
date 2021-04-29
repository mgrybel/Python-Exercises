def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True


result = avoids(word='Python', forbidden='P')
print(result) # prints False
