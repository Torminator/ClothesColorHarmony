import collections
import colorharmony.munsell as munsell

class Outfit():

    def __init__(self, clothes):
        seen = collections.OrderedDict()
        for cloth in clothes:
            if cloth.tag not in seen:
                seen[cloth.tag] = cloth
        self.clothes = seen.values()

    def is_harmonious(self, debug=False):
        munsell_dict = munsell.construct_rgb_to_munsell()
        color_palette = list({munsell_dict[color] for cloth in self.clothes for color in cloth.colors})
        if debug:
            print(color_palette)
        if len(color_palette) == 1:
            return True
        if len(color_palette) == 2:
            complementary_dict = munsell.construct_complementary_colors_in_munsell()
            analogous_dict = munsell.construct_analogous_colors_in_munsell()
            if (
                color_palette[0][0] == color_palette[1][0] or
                complementary_dict[color_palette[0][0]] == color_palette[1][0] or
                analogous_dict[color_palette[0][0]] == color_palette[1][0]
            ):
                return True

        return False
