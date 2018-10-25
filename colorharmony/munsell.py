from os.path import join, dirname, abspath
from colorharmony.nearstkeydict import NearstKeyDict
from scipy.spatial import distance
import csv

def construct_rgb_to_munsell():
    project_path = dirname(dirname(abspath(__file__)))
    with open(join(project_path, "color_tables", "real_sRGB.csv")) as csvfile:
        color_table = csv.reader(csvfile, delimiter=",", quotechar='"')
        # skip header
        next(color_table)
        munsell_dict = {}
        for color in color_table:
            munsell_dict[(eval(color[16]), eval(color[17]), eval(color[18]))] = (color[1], eval(color[2]), eval(color[3]))

    return NearstKeyDict(munsell_dict, distance.euclidean)

def construct_complementary_colors_in_munsell():
    complementary_colors = [('R', 'BG'), ('YR', 'B'), ('Y', 'PB'), ('GY', 'P'), ('G', 'RP')]
    complementary_dict = {}
    for c in complementary_colors:
        for num in [2.5, 5, 7.5, 10]:
            complementary_dict['{}{}'.format(num, c[0])] = '{}{}'.format(num, c[1])
            complementary_dict['{}{}'.format(num, c[1])] = '{}{}'.format(num, c[0])

    return complementary_dict

def construct_analogous_colors_in_munsell():
    analogous_colors = ['RP', 'R', 'YR', 'Y', 'GY', 'G', 'BG', 'B', 'PB', 'P', 'RP', 'R']
    analogous_dict = {}
    for i in range(1, len(analogous_colors)-1):
        for num in [2.5, 5, 7.5, 10]:
            analogous_dict['{}{}'.format(num, analogous_colors[i])] = ('{}{}'.format(num, analogous_colors[i+1]),
                '{}{}'.format(num, analogous_colors[i-1]))
    return analogous_dict
