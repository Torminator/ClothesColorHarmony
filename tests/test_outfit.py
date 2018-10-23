from colorharmony.outfit import Outfit
from colorharmony.cloth import create_cloth_from_image

from os.path import join, dirname, abspath
import pytest

@pytest.fixture
def image_dir():
    return join(dirname(dirname(abspath(__file__))), "clothes_images")

def test_outfit_constructor_normal(image_dir):
    image_path = join(image_dir, "TOB22O01O-K11@10.jpg")
    tshirt = create_cloth_from_image(image_path, "tshirt")
    image_path = join(image_dir, "JA222E06B-N11@12.jpg")
    trouser = create_cloth_from_image(image_path, "trouser")

    assert len(Outfit([tshirt, trouser]).clothes) == 2

def test_outfit_constructor_2tshirt(image_dir):
    image_path = join(image_dir, "TOB22O01O-K11@10.jpg")
    tshirt1 = create_cloth_from_image(image_path, "tshirt")
    image_path = join(image_dir, "SU222O11M-L11@10.jpg")
    tshirt2 = create_cloth_from_image(image_path, "tshirt")

    assert len(Outfit([tshirt1, tshirt2]).clothes) == 1
