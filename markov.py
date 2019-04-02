from bldup import bldup

class markov:
    def __init__(self, base = None, blsize = 1, baseloop = True):
        if base is None:
            base = {0:{0:1}} #default markov chain
        if type(base) == dict:
            self.graph = dict(base)
        else:
            self.graph=dict()
            for t0, t1 in bldup(base, blsize, baseloop): #iterability test (indirect)
                try: self.graph[t0][t1]+=1
                except KeyError:
                    try: self.graph[t0][t1]=1
                    except KeyError:
                        self.graph[t0]={t1:1}
        self.normalize()
    def normalize(self):
        pass
