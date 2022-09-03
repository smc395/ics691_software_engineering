//*******************************************************************
//  __description__ = "Assignment 01 - Unit Testing"
//  __course__ = "cs108"
//  __organization__ = "Information and Computer Sciences Department, University of Hawai‘i at Mānoa"
//  __author__ = "Anthony Peruma"
//  __email__ = "peruma@hawaii.edu"
//  __version__ = "1.0"
//  __created__ = "2022-08-01"
//  __modified__ = "2022-08-07"
//  __maintainer__ = "Anthony Peruma"
//*******************************************************************
package edu.hawaii.ics.peruma;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public class ATM {

    List<Customer> customers;


    public ATM(List<Customer> customers) {
        this.customers = customers;
    }

    public boolean verifyCustomer(int accountNumber, int pin) {
        Optional<Customer> customer = customers.stream().filter(c -> c.getAccountNumber()==accountNumber && c.getPin()==pin).findFirst();
        return customer.isPresent();
    }

    public float getCustomerBalance(int accountNumber, int pin) throws Exception {
        if (verifyCustomer(accountNumber, pin)) {
            Optional<Customer> customer = customers.stream().filter(c -> c.getAccountNumber()==accountNumber && c.getPin()==pin).findFirst();
            return customer.get().getBalance();
        } else {
            throw new Exception("Invalid Customer");
        }
    }

    public boolean withdrawMoney(int accountNumber, int pin,float amount) throws Exception {
        if (verifyCustomer(accountNumber, pin)) {
            Optional<Customer> customer = customers.stream().filter(c -> c.getAccountNumber()==accountNumber && c.getPin()==pin).findFirst();
            float currentBalance = customer.get().getBalance();
            customer.get().setBalance(currentBalance - amount);
            return true;
        } else {
            throw new Exception("Invalid Customer");
        }
    }

}
