
import pytest
from indicatorCalculation.indicator.indicator import (get_difference_in_days,
                                                      datetime_from_iso_date,
                                                      score_award_period,
                                                      get_releases_by_amount_of_bidders,
                                                      get_amount_of_releases_with_only_one_bidder)

import pprint

from indicatorCalculation.json_parser.parser import get_releases, parse_json

TEST_JSON = 'tests/test_data/georgia_small.json'


@pytest.fixture
def releases():
    return get_releases(parse_json(TEST_JSON))


def test_get_difference_in_days():
    '''January 2016 should have 31 days.'''
    assert get_difference_in_days("2016-01-01", "2016-02-01") == 31


@pytest.mark.parametrize("input,expected", [(28, 5),
                                            (50, 2),
                                            (-10, 20),
                                            (0, 6)])
def test_score_award_period(input, expected):
    '''test award period score'''
    assert score_award_period(input) == expected


@pytest.mark.parametrize("input,expected", [("3046-5-2", 3046),
                                            ("1999-12-31", 1999)])
def test_datetime_from_iso_date(input, expected):
    '''Check whether year is the same'''
    assert datetime_from_iso_date(input).year == expected


def test_releases_with_only_one_bidder():
    pass


def test_get_releases_by_amount_of_bidders():

    releases = get_releases(parse_json(TEST_JSON))

    pprint.pprint(get_releases_by_amount_of_bidders(releases).keys())

    assert set(get_releases_by_amount_of_bidders(releases).keys()) == set([0,1,2,3,4])


def test_get_amount_of_releases_with_only_one_bidder(releases):

    assert get_amount_of_releases_with_only_one_bidder(releases) == 4
