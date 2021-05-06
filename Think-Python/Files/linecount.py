filename = '/Users/monika/Desktop/GitHub/Python-Exercises/Think-Python/Case_Study_Data_Structure_Selection/Dracula.txt'

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount(filename))