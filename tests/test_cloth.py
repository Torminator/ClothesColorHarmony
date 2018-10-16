from colorharmony.cloth import from_image_to_colors, load_colortable_as_dict, put_alpha, load_colortypes
from PIL import Image
import pytest
from os.path import join, dirname, abspath

@pytest.fixture
def colorname_table():
    return load_colortable_as_dict()

def test_load_colornametable1(colorname_table):
    assert colorname_table[(128,0,0)] == "maroon"

def test_load_colornametable2(colorname_table):
    assert colorname_table[(124,252,0)] == "lawn green"


@pytest.fixture
def colortype_table():
    return load_colortypes()

def test_load_colortype1(colortype_table):
    assert colortype_table["white"] == "White"

def test_load_colortype2(colortype_table):
    assert colortype_table["teal"] == "Cyan"


def test_cloth_image1():
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "TOB22O01O-K11@10.jpg"))
    put_alpha(image)
    assert from_image_to_colors(image) == ["steel blue"]

def test_cloth_image2():
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "FR622D01L-K12@9.jpg"))
    put_alpha(image)
    assert from_image_to_colors(image) == ["dim gray"]

def test_cloth_image3():
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "1006771_14796_7.jpg"))
    put_alpha(image)
    assert from_image_to_colors(image) == ["ming"]

def test_cloth_image4():
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "M9121N0QY-Q11@12.jpg"))
    put_alpha(image)
    assert from_image_to_colors(image) == ["black"]

def test_cloth_image5():
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "TOB22T016-G11@2.jpg"))
    put_alpha(image)
    assert from_image_to_colors(image) == ["alizarin"]

def test_cloth_image6():
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "PI922SA08-E11@10.jpg"))
    put_alpha(image)
    assert from_image_to_colors(image) == ["yellow"]

def test_cloth_image7():
    project_path = dirname(dirname(abspath(__file__)))
    image = Image.open(join(project_path, "clothes_images", "UR622S03F-T11@13.1.jpg"))
    put_alpha(image)
    assert from_image_to_colors(image) == ["beige", "blue", "red"]
