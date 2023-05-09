#!/usr/bin/python3

import unittest


class Testnumber(unittest.TestCase):

    def test_number(self):
        self.assertEqual(1, 1)

    def test_othernumber(self):
        self.assertTrue(1 != 2)


if __name__ == '__main__':
    unnittest.main()
