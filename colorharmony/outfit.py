import collections
from colorharmony.munsell import Munsell

class Outfit():

    def __init__(self, clothes):
        seen = collections.OrderedDict()
        for cloth in clothes:
            if cloth.tag not in seen:
                seen[cloth.tag] = cloth
        self.clothes = seen.values()

    def is_harmonious(self, debug=False):
        munsell = Munsell()
        color_palette = list({munsell[color] for cloth in self.clothes for color in cloth.colors})
        if debug:
            print(color_palette)
        if len(color_palette) == 1:
            return True
        if len(color_palette) == 2:
            if color_palette[0][0] == color_palette[1][0]:
                return True
            if munsell.is_complementary(color_palette[0], color_palette[1]):
                return True

        return False
