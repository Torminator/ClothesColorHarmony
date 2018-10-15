from colorharmony.nearstkeydict import NearstKeyDict
import pytest

# We test first the 1d case and show that given a measure which has the
# following properties
#   1. d(x,y) => 0
#   2. d(x,x) == 0
#   3. d(x,y) + d(y,z) => d(x,z)
# then the NearstKeyDict will return the value for the nearst key according to the
# measure.
# This means that one has to check if the function provided to the NearstKeyDict
# is a measure for the keys space.
@pytest.fixture
def init_dict1d():
    test_dict = {1: "Hello", 3: "World", 6: "!!!!"}
    nk_dict = NearstKeyDict(test_dict, lambda x,y: abs(x-y))
    return nk_dict

@pytest.fixture
def init_dict1d_reversed():
    test_dict = {6: "!!!!", 3: "World", 1: "Hello"}
    nk_dict = NearstKeyDict(test_dict, lambda x,y: abs(x-y))
    return nk_dict


def test_key_in_dict1d(init_dict1d):
    assert init_dict1d[1] == "Hello"

# Inside the range
def test_1_key_not_in_dict1d(init_dict1d):
    assert init_dict1d[4] == "World"

# Outside the range
def test_2_key_not_in_dict1d(init_dict1d):
    assert init_dict1d[7] == "!!!!"

# The Dict will choose the first key if the unknown_key has the same
# distance to more than one key. For strings or vectors there is no
# ordering. Thus the first key will be chosen. Hence if we reverse the order
# of the dict we will get different results.
def test_key_between_two_keys_dict1d(init_dict1d):
    assert init_dict1d[2] == "Hello"

def test_key_between_two_keys_dict1d_r(init_dict1d_reversed):
    assert init_dict1d_reversed[2] == "World"
