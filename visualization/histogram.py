from bokeh.plotting import quad, output_file, show, xaxis, yaxis

from indicatorCalculation.json_parser.parser import get_number_of_bidders, get_start_date, get_award_date
from indicatorCalculation.indicator.indicator import get_releases_by_amount_of_bidders

output_file("histogram.html", title="Number of bidders frequency")


def create_histogram(releases):

    number_of_bidders_list = []
    frequency_list = []
    for number_of_bidders, corresponding_releases in get_releases_by_amount_of_bidders(releases).items():
        number_of_bidders_list.append(number_of_bidders)
        frequency_list.append(len(corresponding_releases))

    zeros = [0]*len(frequency_list)
    right = [x+1 for x in number_of_bidders_list]
    histogram = quad(top=frequency_list, bottom=zeros, left=number_of_bidders_list, right=right)

    histogram.title = "Frequency of releases vs. Number of Bidders"
    xaxis()[0].axis_label = "Number of Bidders"
    yaxis()[0].axis_label = "Frequency of Releases"

    show()




if __name__ == '__main__':
    from indicatorCalculation.json_parser.parser import parse_json, get_releases
    releases = get_releases(parse_json('tests/test_data/georgia_small.json'))

    create_histogram(releases)