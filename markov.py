
class markov:
    def __init__(self, base=None):
        if base is None:
            base = {0:{0:1}} #default markov chain
        if type(base) == dict:
            self.graph = dict(base)
        else:
            for x in base: #iterability test
                break
        
