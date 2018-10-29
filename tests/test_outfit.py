from colorharmony.outfit import Outfit
from colorharmony.cloth import Cloth

def test_outfit_constructor_normal():
    tshirt = Cloth(tag="tshirt", colors=[(255,255,0)])
    trouser = Cloth(tag="trouser", colors=[(0,0,0)])

    assert len(Outfit([tshirt, trouser]).clothes) == 2

def test_outfit_constructor_2tshirt():
    tshirt1 = Cloth(tag="tshirt", colors=[(128,0,0), (255,255,255)])
    tshirt2 = Cloth(tag="tshirt", colors=[(0,128,0)])

    assert len(Outfit([tshirt1, tshirt2]).clothes) == 1

def test_harmonious_1color():
    tshirt = Cloth(tag="tshirt", colors=[(255,255,0)])
    outfit = Outfit(clothes=[tshirt])

    assert outfit.is_harmonious() is True

def test_harmonious_1color():
    tshirt = Cloth(tag="tshirt", colors=[(255,255,0)])
    outfit = Outfit(clothes=[tshirt])

    assert outfit.is_harmonious() is True

def test_harmonious_1color():
    tshirt = Cloth(tag="tshirt", colors=[(255,255,0)])
    outfit = Outfit(clothes=[tshirt])

    assert outfit.is_harmonious() is True
