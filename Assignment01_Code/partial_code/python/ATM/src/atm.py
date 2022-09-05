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
            return False

    # MC: check if sufficient balance for withdraw amount
    def withdraw_balance_check(self, amount, balance):
        if (balance - amount) < 0.0:
            print(f'Insufficient funds for requested ${amount}. Your balance is ${balance}.')
            return False
        return True

    # MC: check if the amount is not negative
    def valid_amount_check(self, amount):
        if amount < 0.0:
            print('Please input amount greater than zero.')
            return False
        return True

    def withdraw_money(self, account_number, pin, amount):
        if self.verify_customer(account_number, pin):
            customer_record = next((item for item in self.customers if item.get('account') == account_number), None)
            # MC: get customer's balance
            c_balance = customer_record['balance']
            # MC: check withdraw amount is not negative and balance is not negative after withdraw
            if self.withdraw_balance_check(amount, c_balance) and self.valid_amount_check(amount):
                customer_record['balance'] = c_balance - amount
                return True
            else:
                return False
        else:
            return False

    def deposit_money(self, account_number, pin, amount):
        if self.verify_customer(account_number, pin):
            customer_record = next((item for item in self.customers if item.get('account') == account_number), None)
            # MC: check deposit is not negative before adding to balance
            if self.valid_amount_check(amount):
                customer_record['balance'] = customer_record['balance'] + amount
                return True
            else:
                return False
        else:
            return False

    # MC: helper function when changing pin to validate user input
    def valid_pin_check(self, new_pin):
        # MC: check if the pin is not a number. If true then pin is invalid
        if not str(new_pin).isnumeric():
            return False
        # MC: check if the pin is a valid 3-digit pin between 100 and 999
        elif 99 < int(new_pin) < 1000:
            return True
        else:
            return False

    def change_pin(self, account_number, current_pin, new_pin):
        # MC: first check that the person verifies they are the customer
        if self.verify_customer(account_number, current_pin):
            customer_record = next((item for item in self.customers if item.get('account') == account_number), None)
            # MC: if the pin is a valid 3-pin number then change it
            if self.valid_pin_check(new_pin):
                customer_record['pin'] = new_pin
                return True
            else:
                return False
        else:
            return False
