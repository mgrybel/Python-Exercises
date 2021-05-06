import pickle

t = [1, 2, 3]

s = pickle.dumps(t)
print(s)

t2 = pickle.loads(s)
print(t2)