def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(n=3, s=0)