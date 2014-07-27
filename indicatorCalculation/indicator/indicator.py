import datetime
from indicatorCalculation.json_parser.parser import get_number_of_bidders


#def score_number_of_bidders(number_of_bidders):
#    pass


def get_difference_in_days(start_date, end_date):
    '''Takes a start and end iso date string and returns
       the amount of days in between.
    '''

    start_datetime = datetime_from_iso_date(start_date)
    end_datetime = datetime_from_iso_date(end_date)
    delta = end_datetime - start_datetime
    return delta.days


def datetime_from_iso_date(isoDate):
    '''Takes a iso date string and returns a python
       datetime.datetime object
    '''

    return datetime.datetime(*[int(x) for x in isoDate.split('-')])


def score_award_period(number_of_days):
    '''Returns a score for the award period as defined in
       the kd_ted_sample_20140725.do script
    '''

    bins = [(None, -1, 20), (-1, 23, 6), (23, 42, 5), (42, 43, 4),
            (43, 48, 3), (48, 52, 2), (52, None, 1)]

    for lower, upper, score in bins:

        if lower:
            above = lower < number_of_days
        else:
            above = True

        if upper:
            underneath = number_of_days <= upper
        else:
            underneath = True

        if above and underneath:
            return score


def get_releases_by_amount_of_bidders(releases):
    '''Returns a dictionary with the
       number of bidders as the keys and
       lists of releases as the values.
    '''

    releases_by_number = {}
    for release in releases:
        number = get_number_of_bidders(release)
        if number in releases_by_number:
            releases_by_number[number].append(release)
        else:
            releases_by_number[number] = [release]
    return releases_by_number


def get_amount_of_releases_with_only_one_bidder(releases):
    '''Returns and int with the number of releases
       with only one bidder.
    '''

    return len(get_releases_by_amount_of_bidders(releases).get(1,[]))

