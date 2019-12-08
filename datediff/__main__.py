"""datediff entry point."""

import argparse

from datediff.date import Date


def str_to_date(date, delim='/'):
    """
    Convert date string to day, month, year.

    :param date: date to be converted
    :param delim: delimiter that separates fields in date
    :returns: (day, month, year)
    """
    return map(int, date.split(delim))


def main():
    """Compute diff between dates."""
    parser = argparse.ArgumentParser(
        description='Difference between two dates')
    parser.add_argument('start_date', help='start date')
    parser.add_argument('dash_sep', metavar='-', help='dash separator')
    parser.add_argument('end_date', help='start date')

    args = parser.parse_args()

    start_date = Date(*str_to_date(args.start_date))
    end_date = Date(*str_to_date(args.end_date))

    print(f'{end_date - start_date}')


if __name__ == '__main__':
    # need this if block to avoid calling main() twice by entry_points
    main()
