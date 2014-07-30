import json

from pprint import pprint


def parse_json(filePath):

    with open(filePath, 'r') as f:
        read_data = f.read()
        parsed = json.loads(read_data)
        return parsed


def get_releases(parsed_json):
    try:
        return parsed_json["releases"]
    except KeyError:
        return None


def get_release_ID(release):
    try:
        return release["releaseMeta"]["releaseID"]
    except KeyError:
        return None


def get_number_of_bidders(release):
    try:
        return int(release["formation"]["numberOfBidders"])
    except KeyError:
        return None


def get_start_date(release):
    try:
        return release["formation"]["notice"]["publishedDate"]
    except (KeyError, TypeError):
        return None


def get_award_date(release):
    try:
        return release["formation"]["awardPeriod"]["endDate"]
    except KeyError:
        return None

def get_total_value_amount(release):

    try:
        return release["formation"]["totalValue"]["amount"]
    except KeyError:
        return None