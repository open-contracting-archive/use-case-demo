import pytest

from indicatorCalculation.json_parser.parser import parse_json, get_releases, get_release_ID, get_start_date, get_award_date, get_number_of_bidders
#from indicatorCalculation.json_parser.parser import parse_json

TEST_JSON = 'tests/test_data/georgia_small.json'

@pytest.fixture
def parsed_json():
    return parse_json(TEST_JSON)

@pytest.fixture
def release():
    return get_releases(parse_json(TEST_JSON))[0]

def test_get_release_ID(release):
    assert get_release_ID(release) == '1'

def test_get_release_ID_with_empty_Dict():
    assert get_release_ID(dict()) == None

def test_get_number_of_bidders(release):
    assert get_number_of_bidders(release) == 1

def test_get_start_date(release):
    assert get_start_date(release) == "2013-06-11"

def test_get_award_date(release):
    assert get_award_date(release) == "2013-07-03"

