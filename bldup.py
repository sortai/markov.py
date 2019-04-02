def bldup(x, s=1):
    l = len(x)
    for i in range(l):
        if i>=l-s: break
        yield (x[i:i+s],x[i+1:i+s+1])
