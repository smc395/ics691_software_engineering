"""
__description__ = "Assignment 01 - Unit Testing"
__course__ = "ics691E"
__organization__ = "Information and Computer Sciences Department, University of Hawai‘i at Mānoa"
__author__ = "Sung Yan Micah Chao (sungyanc)"
__email__ = "sungyanc at hawaii dot edu"
__code_version__ = "1.0"
__python_version__ = "3.8"
__created__ = "2022-09-01"
__modified__ = "2022-09-03"
__maintainer__ = "Micah Chao"
"""

import coverage
import sys

cov = coverage.Coverage()
cov.start() # start code coverage

sys.path.insert(0, "..\\src\\")  # add src folder to path for python to read

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from atm import ATM



class TestATM(TestCase):

    def setUp(self):
        self.customers = []
        self.customers.append({'account': 12345, 'pin': 555, 'balance': 1200.0})
        self.customers.append({'account': 45454, 'pin': 111, 'balance': 33.33})
        self.customers.append({'account': 98765, 'pin': 999, 'balance': 0.0})

        self.atm = ATM(self.customers)

    @classmethod
    def tearDownClass(self):
        cov.stop() # stop code coverage
        cov.save() # save results
        cov.html_report() # generate html report of coverage

    # assert that the verify_customer method returns True with correct pin and False with incorrect pin
    def test_verify_valid_customer(self):
        self.assertTrue(self.atm.verify_customer(12345, 555))
        self.assertFalse(self.atm.verify_customer(12345, 000))

    # valid_amount_check() tests
    # assert that numbers greater than or equal to zero return True
    def test_valid_amount_check(self):
        self.assertTrue(self.atm.valid_amount_check(0.0))
        self.assertTrue(self.atm.valid_amount_check(1.0))
        self.assertTrue(self.atm.valid_amount_check(1))

    # assert that negative amounts return False and prints error statement
    def test_valid_amount_check_negative_amount(self):
        expected_neg_amt_str = 'Please input amount greater than zero.\n'
        self.assertFalse(self.atm.valid_amount_check(-1))
        self.assertFalse(self.atm.valid_amount_check(-1.0))
        with patch('sys.stdout', new=StringIO()) as neg_amt_str:
            self.atm.valid_amount_check(-7)
            self.assertEqual(neg_amt_str.getvalue(), expected_neg_amt_str)

    # withdraw_balance_check() tests
    # assert if amount equals balance return True
    # assert if amount is less than balance return True
    def test_withdraw_balance_check(self):
        self.assertTrue(self.atm.withdraw_balance_check(100, 100))
        self.assertTrue(self.atm.withdraw_balance_check(25, 100))

    # assert if withdraw amount is greater than balance return False and prints error statement
    def test_withdraw_balance_check_insufficient_balance(self):
        expected_insuff_bal_str = 'Insufficient funds for requested $50. Your balance is $20.\n'
        self.assertFalse(self.atm.withdraw_balance_check(50, 20))
        self.assertFalse(self.atm.withdraw_balance_check(50.0, 20.0))
        self.assertFalse(self.atm.withdraw_balance_check(41.0, 40.99))
        with patch('sys.stdout', new=StringIO()) as insuff_bal_str:
            self.atm.withdraw_balance_check(50, 20)
            self.assertEqual(insuff_bal_str.getvalue(), expected_insuff_bal_str)

    # withdraw_money() tests
    # assert that withdrawing amount less than balance correctly reduces balance by amount requested
    def test_withdraw_money(self):
        self.atm.withdraw_money(45454, 111, 3.33)
        balance = self.atm.get_customer_balance(45454, 111)
        self.assertEqual(30.0, balance)

    # assert that using an invalid pin does not withdraw money
    def test_withdraw_money_invalid_pin(self):
        self.assertFalse(self.atm.withdraw_money(45454, 888, 3.33))
        balance = self.atm.get_customer_balance(45454, 111)
        self.assertEqual(33.33, balance)

    # assert that withdrawing zero money does not change balance
    def test_withdraw_zero_money(self):
        self.atm.withdraw_money(45454, 111, 0.0)
        balance = self.atm.get_customer_balance(45454, 111)
        self.assertEqual(33.33, balance)

    # assert that withdrawing negative money does not change balance
    def test_withdraw_money_negative_amount(self):
        self.assertFalse(self.atm.withdraw_money(12345, 555, -1.1))
        balance = self.atm.get_customer_balance(12345, 555)
        self.assertEqual(1200.0, balance)

    # assert that withdrawing to withdraw more than balance does not change balance
    def test_withdraw_money_insufficient_funds(self):
        self.assertFalse(self.atm.withdraw_money(98765, 999, 100))
        balance = self.atm.get_customer_balance(98765, 999)
        self.assertEqual(0.0, balance)


    # get_customer_balance() tests
    # assert that correct pin and account returns balance
    def test_get_customer_balance(self):
        balance = self.atm.get_customer_balance(12345, 555)
        self.assertEqual(1200.0, balance)

    # assert that incorrect account and pin returns False
    def test_get_customer_balance_invalid_customer(self):
        self.assertFalse(self.atm.get_customer_balance(000, 000))

    # deposit_money() tests
    # assert that depositing money with non-negative amount changes balance
    def test_deposit_money_zero_money(self):
        # assert adding nothing does not change balance
        self.assertTrue(self.atm.deposit_money(12345, 555, 0.0))
        self.assertEqual(self.atm.get_customer_balance(12345, 555), 1200.0)

    # assert deposit amount changes balance correctly
    def test_deposit_money(self):
        self.assertTrue(self.atm.deposit_money(12345, 555, 100.0))
        self.assertEqual(self.atm.get_customer_balance(12345, 555), 1300.0)

        self.assertTrue(self.atm.deposit_money(12345, 555, 1.1))
        self.assertEqual(self.atm.get_customer_balance(12345, 555), 1301.1)

    # assert that depositing negative money returns False
    def test_deposit_money_negative_amount(self):
        self.assertFalse(self.atm.deposit_money(12345, 555, -100.0))
        self.assertFalse(self.atm.deposit_money(12345, 555, -6))

    # assert that using the wrong pin when depositing does not change balance
    def test_deposit_money_invalid_pin(self):
        self.assertFalse(self.atm.deposit_money(12345, 333, 100.0))
        balance = self.atm.get_customer_balance(12345, 555)
        self.assertEqual(1200.0, balance)

    # valid_pin_check() tests
    # assert that edge case numbers and number in pin range returns Ture
    def test_valid_pin_check(self):
        self.assertTrue(self.atm.valid_pin_check(777))
        self.assertTrue(self.atm.valid_pin_check(100))
        self.assertTrue(self.atm.valid_pin_check(999))

    # assert that entering non-numeric pins returns False
    def test_valid_pin_check_alpha_pin(self):
        self.assertFalse(self.atm.valid_pin_check('abc'))
        self.assertFalse(self.atm.valid_pin_check('77a'))
        self.assertFalse(self.atm.valid_pin_check('0*a'))

    # assert that numeric pins as strings returns True
    def test_valid_pin_check_str_number(self):
        self.assertTrue(self.atm.valid_pin_check('999'))

    # assert that numbers outside of requirements range returns False
    def test_valid_pin_check_bad_numeric_pin(self):
        self.assertFalse(self.atm.valid_pin_check(-555))
        self.assertFalse(self.atm.valid_pin_check(99))
        self.assertFalse(self.atm.valid_pin_check(1000))

    # change_pin() tests
    # assert that change pin functionality changes pin to user input
    def test_change_pin(self):
        # assert pin gets changed correctly
        self.assertTrue(self.atm.change_pin(12345, 555, 888))

        # assert old pin does not work
        self.assertFalse(self.atm.get_customer_balance(12345, 555))

        # assert new pin works to get balance
        self.assertEqual(self.atm.get_customer_balance(12345, 888), 1200.0)

    # assert that invalid pin to verify customer returns False
    def test_change_pin_wrong_verify_pin(self):
        self.assertFalse(self.atm.change_pin(12345, 222, 888))

    # assert that pin outside range returns False
    def test_change_pin_invalid_pin(self):
        self.assertFalse(self.atm.change_pin(12345, 555, 1))
        self.assertFalse(self.atm.change_pin(12345, 555, -1))
        self.assertFalse(self.atm.change_pin(12345, 555, 1000))
