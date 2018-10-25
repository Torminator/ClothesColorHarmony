import collections

class Outfit():

    def __init__(self, clothes):
        seen = collections.OrderedDict()
        for cloth in clothes:
            if cloth.tag not in seen:
                seen[cloth.tag] = cloth
        self.clothes = seen.values()

    def is_harmonious():
        return True
