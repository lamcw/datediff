import unittest

from datediff.date import Date


class TestLeapYear(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(Date(year=4)._n_leap_years(), 0)
        self.assertEqual(Date(month=3, year=4)._n_leap_years(), 1)
        self.assertEqual(Date(year=100)._n_leap_years(), 24)
        self.assertEqual(Date(month=3, year=100)._n_leap_years(), 24)
        self.assertEqual(Date(year=400)._n_leap_years(), 96)
        self.assertEqual(Date(month=3, year=400)._n_leap_years(), 97)
        self.assertEqual(Date(month=3, year=800)._n_leap_years(), 194)

    def test_non_leap(self):
        self.assertEqual(Date(year=3)._n_leap_years(), 0)
        self.assertEqual(Date(year=7)._n_leap_years(), 1)
        self.assertEqual(Date(year=101)._n_leap_years(), 24)
        self.assertEqual(Date(year=403)._n_leap_years(), 97)


class TestDate(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Date(), Date())
        self.assertNotEqual(Date(year=2000), Date(year=2001))
        self.assertNotEqual(Date(), Date(month=2))
        self.assertNotEqual(Date(), Date(day=2))

    def test_simple_elapse(self):
        self.assertEqual(Date(7, 11, 1972) - Date(7, 11, 1972), 0)
        self.assertEqual(Date(7, 11, 1972) - Date(8, 11, 1972), 0)
        self.assertEqual(Date(1, 1, 2000) - Date(3, 1, 2000), 1)

    def test_diff(self):
        self.assertEqual(Date(22, 6, 1983) - Date(2, 6, 1983), 19)
        self.assertEqual(Date(25, 12, 1984) - Date(4, 7, 1984), 173)
        self.assertEqual(Date(3, 8, 1983) - Date(3, 1, 1989), 1979)
