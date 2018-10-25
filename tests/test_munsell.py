import pytest
from colorharmony.munsell import construct_rgb_to_munsell, construct_complementary_colors_in_munsell, construct_analogous_colors_in_munsell


@pytest.fixture
def rgb_to_munsell():
    return construct_rgb_to_munsell()

def test_rgb_to_munsell1(rgb_to_munsell):
    assert rgb_to_munsell[(166, 144, 143)] == ('5R', 6, 2)

@pytest.fixture
def analogous_colors():
    return construct_analogous_colors_in_munsell()

def test_analogous_colors1(analogous_colors):
    assert analogous_colors['2.5R'] == ('2.5YR', '2.5RP')

def test_analogous_colors2(analogous_colors):
    assert analogous_colors['5GY'] == ('5G', '5Y')

def test_analogous_colors3(analogous_colors):
    assert analogous_colors['7.5B'] == ('7.5PB', '7.5BG')

def test_analogous_colors4(analogous_colors):
    assert analogous_colors['10PB'] == ('10P', '10B')

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
