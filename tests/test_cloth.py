from colorharmony.cloth import Cloth, create_cloth_from_image, load_colortable_as_dict
import pytest
from os.path import join, dirname, abspath

@pytest.fixture
def colorname_table():
    return load_colortable_as_dict()

def test_load_colornametable1(colorname_table):
    assert colorname_table[(128,0,0)] == "maroon"

def test_load_colornametable2(colorname_table):
    assert colorname_table[(124,252,0)] == "lawn green"

# Because the clusters are learned by the kmeans algorithm. There is no good
# way (maybe there is?) to test the cluster centers. Thus i check if the right
# number of colors have been detected.
@pytest.fixture
def image_dir():
    return join(dirname(dirname(abspath(__file__))), "clothes_images")

def test_cloth_image1(image_dir):
    image_path = join(image_dir, "TOB22O01O-K11@10.jpg")
    assert len(create_cloth_from_image(image_path, "tshirt").colors) == 1

def test_cloth_image2(image_dir):
    image_path = join(image_dir, "FR622D01L-K12@9.jpg")
    assert len(create_cloth_from_image(image_path, "shirt").colors) == 1

def test_cloth_image3(image_dir):
    image_path = join(image_dir, "1006771_14796_7.jpg")
    assert len(create_cloth_from_image(image_path, "hoodie").colors) == 1

def test_cloth_image4(image_dir):
    image_path = join(image_dir, "M9121N0QY-Q11@12.jpg")
    assert len(create_cloth_from_image(image_path, "jeans").colors) == 1

def test_cloth_image5(image_dir):
    image_path = join(image_dir, "TOB22T016-G11@2.jpg")
    assert len(create_cloth_from_image(image_path, "jacket").colors) == 1

def test_cloth_image6(image_dir):
    image_path = join(image_dir, "PI922SA08-E11@10.jpg")
    assert len(create_cloth_from_image(image_path, "hoodie").colors) == 1

def test_cloth_image7(image_dir):
    image_path = join(image_dir, "UR622S03F-T11@13.1.jpg")
    assert len(create_cloth_from_image(image_path, "sweater").colors) == 3
