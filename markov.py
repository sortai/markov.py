from random import random

def rchoose(d):
    t = 0
    for co in d:
        t += d[co]
    i = t*random()
    for co in d:
        if d[co] > i: return co
        else: i -= d[co]

class markov:
    def __init__(self, base = None, plen = 1):
        if base is None:
            base = {0:{0:1}} #default markov chain
        if type(base) == dict:
            self.pats = dict(base)
        else:
            self.pats = dict()
            for i in range(len(base)-plen+1):
                try: self.pats[base[i:i+plen]] += 1
                except KeyError: self.pats[base[i:i+plen]] = 1
    def apply(self, base, n = 1, over = None):
        bls = dict()
        for co in self.pats:
            if over is None:
                for ov in range(1,len(co)+1):
                    ob = base[-ov:]
                    op = co[:ov]
                    if ob == op:
                        try: bls[co[ov:]] += self.pats[co]
                        except KeyError: bls[co[ov:]] = self.pats[co]
            else:
                ob = base[-over:]
                op = co[:over]
                if ob == op:
                    try: bls[co[over:]] += self.pats[co]
                    except KeyError: bls[co[over:]] = self.pats[co]
        if n <= 0: return bls
        obls = bls
        bls = dict()
        for co in obls:
            try: bls[co[:n]] += obls[co]
            except KeyError: bls[co[:n]] = obls[co]
        oobls = obls
        obls = bls
        bls = dict()
        for co in obls:
            if len(co) == n: bls[co] = obls[co]
        for co in obls:
            if len(co) < n:
                for tco in bls:
                    if tco.startswith(co): bls[tco]+=obls[co]
        return bls
    def complete(self, base, n=0, over = None):
        pco = self.apply(base, n, over)
        return rchoose(pco)
