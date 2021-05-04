s = 'Monty Python'

slice1 = s[0:5]
print(slice1)

slice2 = s[6:12]
print(slice2)

fruit = 'banana'

slice3 = fruit[:3]
print(slice3)

slice4 = fruit[3:]
print(slice4)

slice5 = fruit[3:3]
print(slice5)

slice6 = fruit[:]
print(slice6)

# the 3rd index specifies the 'step size'
# a step size of -1 goes through the word backwards,
# so the slice [::-1] generates a reversed string
slice7 = fruit[::-1]
print(slice7)