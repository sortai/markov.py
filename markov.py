
class markov:
    def __init__(self, base=None):
        if base is None:
            base = {0:{0:1}} #default markov chain
        if type(base) == dict:
            self.graph = dict(base)
        else:
            try:
                for x in base:
                    break
            except TypeError as e:
                raise TypeError("base template is not iterable").with_traceback(e.__traceback__)
        
