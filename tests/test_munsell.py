import pytest
from colorharmony.munsell import Munsell, construct_analogous_colors_in_munsell, construct_complementary_colors_in_munsell


@pytest.fixture
def munsell():
    return Munsell()

def test_rgb_to_munsell1(munsell):
    assert munsell[(166, 144, 143)] == ('5R', 6, 2)

def test_munsell_complementary(munsell):
    assert munsell.is_complementary(('5R', 6, 2), ('5BG', 6, 2)) is True

def test_munsell_not_complementary1(munsell):
    assert munsell.is_complementary(('5R', 6, 2), ('5PB', 6, 3)) is False

def test_munsell_not_complementary2(munsell):
    assert munsell.is_complementary(('5R', 6, 2), ('5PB', 7, 2)) is False

def test_munsell_not_complementary3(munsell):
    assert munsell.is_complementary(('5R', 6, 2), ('5R', 6, 2)) is False

@pytest.fixture
def analogous_colors():
    return construct_analogous_colors_in_munsell()

def test_analogous_colors1(analogous_colors):
    assert analogous_colors['2.5R'] == ('10RP', '5R')

def test_analogous_colors2(analogous_colors):
    assert analogous_colors['5GY'] == ('2.5GY', '7.5GY')

def test_analogous_colors3(analogous_colors):
    assert analogous_colors['7.5B'] == ('5B', '10B')

def test_analogous_colors4(analogous_colors):
    assert analogous_colors['10PB'] == ('7.5PB', '2.5P')

@pytest.fixture
def complementary_colors():
    return construct_complementary_colors_in_munsell()

def test_complementary_colors1(complementary_colors):
    assert complementary_colors['2.5R'] == '2.5BG'

def test_complementary_colors2(complementary_colors):
    assert complementary_colors['5GY'] == '5P'

def test_complementary_colors3(complementary_colors):
    assert complementary_colors['7.5B'] == '7.5YR'

def test_complementary_colors4(complementary_colors):
    assert complementary_colors['10PB'] == '10Y'
