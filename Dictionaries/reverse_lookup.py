from histogram import histogram

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


h = histogram('parrot')
k = reverse_lookup(h, 2)
print(k) # prints r