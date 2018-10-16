import collections
import itertools
from os.path import dirname, abspath, join
import csv
from colorharmony.nearstkeydict import NearstKeyDict
# from nearstkeydict import NearstKeyDict
from scipy.spatial import distance
from PIL import Image, ImageFilter

cloth = collections.namedtuple("tag", "colors")

def from_image_to_colors(image, debug=False):
    image = image.resize((64,92), Image.LANCZOS)
    #image.show()
    colors = image.getcolors(1000000)
    colorname_table = load_colortable_as_dict()
    colors_in_image = collections.defaultdict(int)
    for color in colors:
        if color[1][-1] == 0:
            continue
        colors_in_image[colorname_table[color[1][:-1]]] += color[0]

    colored_pixels = sum([val for val in colors_in_image.values()])
    print(colored_pixels*0.1)

    colors_list = sorted({k: v for k,v in colors_in_image.items() if v > colored_pixels*0.1},
                    key=colors_in_image.get, reverse=True)

    colortypes = load_colortypes()

    colortypes_in_image = [colortypes[color] for color in colors_list]
    unique_colortypes = set(colortypes_in_image)

    if debug:
        print(colors_in_image)

    for u_c in unique_colortypes:
        u_c_indicies = [index for index, colortype in enumerate(colortypes_in_image)
                            if colortype == u_c]

    return [colors_list[colortypes_in_image.index(u_c)] for u_c in unique_colortypes]

def load_colortable_as_dict():
    project_path = dirname(dirname(abspath(__file__)))
    with open(join(project_path, "colorname_table_random.csv")) as csvfile:
        colorname_table = csv.reader(csvfile, delimiter=",", quotechar='"')
        # skip header
        next(colorname_table)
        colorname_dict = {}
        for color in colorname_table:
            colorname_dict[eval(color[1])] = color[0]

    return NearstKeyDict(colorname_dict, distance.euclidean)

def load_colortypes():
    project_path = dirname(dirname(abspath(__file__)))
    with open(join(project_path, "colorname_table_random.csv")) as csvfile:
        colorname_table = csv.reader(csvfile, delimiter=",", quotechar='"')
        # skip header
        next(colorname_table)
        colortype_dict = {}
        for color in colorname_table:
            colortype_dict[color[0]] = color[2]

    return colortype_dict

def put_alpha(image):
    image_threshold = image.convert(mode="L").point(lambda i: i < 245 and 255)
    image.putalpha(image_threshold)



if __name__ == "__main__":
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "S1721C052-Q11@5.1.jpg"))
    put_alpha(image)
    image.show()

    colors = from_image_to_colors(image, debug=True)#

    print(colors)
