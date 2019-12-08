"""Date implmentation."""
from functools import total_ordering


@total_ordering
class Date:
    """
    Simple date representation.

    >>> Date()
    1/1/1901
    >>> Date(year=2012)
    1/1/2012
    >>> d = Date(3, 12, 2012)
    3/12/2012
    >>> d.day
    3
    >>> d == Date(3, 12, 2012)
    True
    >>> d - Date(2, 12, 2012)
    0
    >>> d - Date(1, 12, 2012)
    1
    """

    MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day=1, month=1, year=1901):  # noqa: D107
        if day <= 0 or day > max(self.MONTH_DAYS):
            raise ValueError("Day out of range")
        if month <= 0 or month > len(self.MONTH_DAYS):
            raise ValueError("Month out of range")
        if year <= 0:
            raise ValueError("Year cannot be smaller or equal to 0")
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):  # noqa: D102
        return self._day

    @property
    def month(self):  # noqa: D102
        return self._month

    @property
    def year(self):  # noqa: D102
        return self._year

    def _n_leap_years(self):
        """
        Find number of leap years before this date.

        A year `y` is a leap year if:
            y % 4 == 0 and (y % 100 != 0 or year % 400 == 0)

        :returns: number of leap years
        """
        y = self.year

        # don't need to check this year if month before March
        if self.year > 0 and self.month < 3:
            y -= 1

        return y // 4 - y // 100 + y // 400

    def _n_days(self):
        """
        Find number of days before this date.

        Assuming gregorian calendar, we can count the number of days by
        `days_in_non_leap_year` + `days_in_month` + `day` + `n_leap_years`.

        :returns: number of days
        """
        days = self.year * sum(self.MONTH_DAYS) + self.day
        for m in range(self.month):
            days += self.MONTH_DAYS[m]
        return days + self._n_leap_years()

    def __eq__(self, other):  # noqa: D105
        return isinstance(other,
                          type(self)) and self.__dict__ == other.__dict__

    def __lt__(self, other):  # noqa: D105
        return self.year < other.year or self.month < other.month \
            or self.day < other.day

    def __sub__(self, other):
        """Difference of dates in days."""
        days = self._n_days()
        days_other = other._n_days()
        return max(max(days, days_other) - min(days, days_other) - 1, 0)

    def __str__(self):
        """Date delimited by slashes(/)."""
        return f'{self.day}/{self.month}/{self.year}'

    __repr__ = __str__
