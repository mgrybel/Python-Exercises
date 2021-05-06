import os

filename = '/Users/monika/Desktop/GitHub/Python-Exercises/Think-Python/Case_Study_Data_Structure_Selection/Dracula.txt'

cmd = 'md5sum' + filename

fp = os.popen(cmd)
res = fp.read()
stat = fp.close()

print(res)
print(stat)