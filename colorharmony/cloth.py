import collections
from os.path import dirname, abspath, join
import csv
from colorharmony.nearstkeydict import NearstKeyDict
from scipy.spatial import distance
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

Cloth = collections.namedtuple("Cloth", ["tag", "colors"])

def create_cloth_from_image(image_path, tag, min_area_in_perecent=0.1, debug=False):
    image_data = load_preprocess_image(image_path)
    colors = cluster_image_into_colors(image_data, min_area_in_perecent, debug)
    return Cloth(tag=tag, colors=colors)

def load_preprocess_image(image_path):
    image = Image.open(image_path)
    # Set the background to transparent
    image_threshold = image.convert(mode="L").point(lambda i: i < 245 and 255)
    image.putalpha(image_threshold)
    image = image.resize((64,92), Image.LANCZOS)
    return np.array(image.getdata())

def cluster_image_into_colors(image_data, min_area_in_perecent, debug):
    colors_count_list = []
    for n in range(2, 11):
        kmeans = KMeans(n_clusters=n, random_state=101).fit(image_data)
        # First filter every color center with an alpha smaller than 200.
        # It means it is a background color.
        colors_count = {tuple(np.round(center[:-1])): sum(kmeans.labels_ == index)
                        for index, center in enumerate(kmeans.cluster_centers_)
                        if center[-1] > 200}
        # Second filter every color center which area is too small
        total_cloth_pixels = sum(count for count in colors_count.values())
        colors_count = {key: count for key, count in colors_count.items()
                        if count > min_area_in_perecent*total_cloth_pixels}

        colors_count_list.append(colors_count)

        if debug:
            print(n)
            print(kmeans.cluster_centers_)
            print(colors_count)
            print("----------------")

        # rules to decide when to stop searching for better colors
        # to compare we need a first entry
        if n == 2:
            continue

        if len(colors_count) > len(colors_count_list[n-3]):
            distance_pairwise = distance.cdist(list(colors_count_list[n-3].keys()),
                                    list(colors_count.keys()))
            for row in distance_pairwise:
                for distance1 in row:
                    for distance2 in row:
                        if distance1 == distance2:
                            break
                        if abs(distance1 - distance2) < 30 and distance1 < 50 and distance2 < 50:
                            return list(colors_count_list[n-3].keys())
        else:
            if n > 3:
                if len(colors_count) == len(colors_count_list[n-4]):
                    return list(colors_count_list[n-3].keys())
    return list(colors_count_list[-1].keys())

def load_colortable_as_dict():
    project_path = dirname(dirname(abspath(__file__)))
    with open(join(project_path, "color_tables", "colorname_table_random.csv")) as csvfile:
        colorname_table = csv.reader(csvfile, delimiter=",", quotechar='"')
        # skip header
        next(colorname_table)
        colorname_dict = {}
        for color in colorname_table:
            colorname_dict[eval(color[1])] = color[0]

    return NearstKeyDict(colorname_dict, distance.euclidean)
