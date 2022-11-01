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

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ATMTest {

    ATM atm;

    @BeforeEach
    void setUp() {
        List<Customer> customers = new ArrayList<>();
        customers.add(new Customer(12345,555,1200.0f));
        customers.add(new Customer(45454,111,33.33f));
        customers.add(new Customer(98765,999,0.0f));

        atm = new ATM(customers);
    }

    @Test
    void verifyValidCustomer() {
        boolean status = atm.verifyCustomer(12345, 555);
        assertTrue(status);
    }

    @Test
    void getCustomerBalance() throws Exception {
        float balance = atm.getCustomerBalance(45454,111);
        assertEquals(33.33f,balance);
    }

    @Test
    void withdrawMoneySuccessful() throws Exception {
        boolean result = atm.withdrawMoney(45454,111,30.0f);
        assertTrue(result);
    }

    @Test
    void getBalanceForInValidCustomerThrowsException() {
        Throwable exception = assertThrows(Exception.class, () -> atm.getCustomerBalance(999,111));
        assertEquals("Invalid Customer", exception.getMessage());
    }
}