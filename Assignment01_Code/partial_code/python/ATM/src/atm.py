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


class ATM:
    customers = []

    def __init__(self, data):
        self.customers = data

    def verify_customer(self, account_number, pin):
        customer_record = next((item for item in self.customers if item.get('account') == account_number), None)
        if customer_record is None:
            return False

        if customer_record['pin'] != pin:
            return False

        return True

    def get_customer_balance(self, account_number, pin):
        if self.verify_customer(account_number, pin):
            customer_balance = next((item for item in self.customers if item.get('account') == account_number), None)['balance']
            return customer_balance
        else:
            return None

    def withdraw_money(self, account_number, pin, amount):
        if self.verify_customer(account_number, pin):
            customer_record = next((item for item in self.customers if item.get('account') == account_number), None)
            customer_record['balance'] = customer_record['balance'] - amount
            return True
        else:
            return False

