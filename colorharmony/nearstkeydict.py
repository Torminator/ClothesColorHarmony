import collections

class NearstKeyDict(collections.UserDict):

    def __init__(self, mapping, measure):
        self.data = dict(mapping)
        self.measure = measure

    def __missing__(self, unknown_key):
        nearst_key = min(self.data.keys(), key=lambda k: self.measure(k,
                                                                unknown_key))
        return self.data[nearst_key]
