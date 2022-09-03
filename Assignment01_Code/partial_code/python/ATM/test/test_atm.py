"""
__description__ = "Assignment 01 - Unit Testing"
__course__ = "ics691E"
__organization__ = "Information and Computer Sciences Department, University of Hawai‘i at Mānoa"
__author__ = "Sung Yan Micah Chao (sungyanc)"
__email__ = "sungyanc at hawaii dot edu"
__version__ = "1.0"
__created__ = "2022-09-01"
__modified__ = "2022-09-01"
__maintainer__ = "Micah Chao"
"""


from unittest import TestCase

from atm import ATM


class TestATM(TestCase):

    def setUp(self):
        self.customers = []
        self.customers.append({'account': 12345, 'pin': 555, 'balance': 1200.0})
        self.customers.append({'account': 45454, 'pin': 111, 'balance': 33.33})
        self.customers.append({'account': 98765, 'pin': 999, 'balance': 0.0})

        self.atm = ATM(self.customers)

    def test_verify_valid_customer(self):
        self.assertTrue(self.atm.verify_customer(12345, 555))

    def test_get_customer_balance(self):
        balance = self.atm.get_customer_balance(12345, 555)
        self.assertEqual(1200.0, balance)

    def test_withdraw_money(self):
        self.atm.withdraw_money(45454, 111, 3.33)
        balance = self.atm.get_customer_balance(45454, 111)
        self.assertEqual(30.0, balance)

    def test_get_customer_balance_invalid_customer(self):
        self.assertFalse(self.atm.get_customer_balance(000, 000))
