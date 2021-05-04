path = '/Users/monika/Desktop/GitHub/Think-Python/Case Study: Word Play/'
filename = 'words.txt'
my_file = path + filename
fin = open(my_file)

for line in fin:
    word = line.strip()
    print(word)
