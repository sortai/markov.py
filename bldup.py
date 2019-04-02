def bldup(x, s=1, loop=True):
    l = len(x)
    for i in range(l):
        if i>=l-s:
            if loop:
                yield (x[i:i+s]+x[0:i+s-l],x[i+1:i+s+1]+x[0:i+s-l+1])
            else: break
        else: yield (x[i:i+s],x[i+1:i+s+1])
