list1 = ['a', 'b', 1, 3.75, [1, 2, 'd', 'e']]

result1 = list1[3:5]
print(result1) # prints [3.75, [1, 2, 'd', 'e']]

result2 = list1[:4]
print(result2) # prints ['a', 'b', 1, 3.75]

result3 = list1[3:]
print(result3) # prints [3.75, [1, 2, 'd', 'e']]

result4 = list1[:]
print(result4) # prints ['a', 'b', 1, 3.75, [1, 2, 'd', 'e']]

list1[1:3] = [2.25, 'cat']
print(list1) # prints ['a', 2.25, 'cat', 3.75, [1, 2, 'd', 'e']]