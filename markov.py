class markov:
    def __init__(self, base = None, blsize = 1):
        if base is None:
            base = {0:{0:1}} #default markov chain
        if type(base) == dict:
            self.pats = dict(base)
        else:
            self.pats=dict()
            for i in range(len(base)-blsize+1):
                try: self.pats[base[i:i+blsize]]+=1
                except KeyError: self.pats[base[i:i+blsize]]=1
