from bokeh.plotting import scatter, show, output_file, curplot, xaxis, yaxis

from indicatorCalculation.json_parser.parser import get_number_of_bidders, get_start_date, get_award_date
from indicatorCalculation.indicator.indicator import get_difference_in_days

output_file("scatterplot.html", title="period between start of tender period and award date vs amount of bidders")


def create_scatter_plot(releases):

    number_of_bidders = []
    delta_time = []

    for release in releases:
        start = get_start_date(release)
        award = get_award_date(release)
        delta = get_difference_in_days(start, award)

        delta_time.append(delta)
        number_of_bidders.append(get_number_of_bidders(release))

    scatter_plot = scatter(delta_time, number_of_bidders,
                           fill_alpha=0.2, size=10,
                           name="period between start of tender period and award date vs amount of bidders")

    scatter_plot.title = "period vs. bidders"
    xaxis()[0].axis_label = "Days"
    yaxis()[0].axis_label = "Number of Bidders"

    show()


if __name__ == '__main__':
    from indicatorCalculation.json_parser.parser import parse_json, get_releases
    releases = get_releases(parse_json('tests/test_data/georgia.json'))

    create_scatter_plot(releases)
