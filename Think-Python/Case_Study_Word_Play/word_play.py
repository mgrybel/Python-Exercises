path = '/Users/monika/Desktop/GitHub/Python-Exercises/Think-Python/Case_Study_Word_Play/'
filename = 'words.txt'
my_file = path + filename
fin = open(my_file)

for line in fin:
    word = line.strip()
    print(word)
