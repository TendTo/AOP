package com.tend.model;


import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.tend.model.Account;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class AccountTest {
    private Account account;

    @BeforeAll
    private void init() {
        account = new Account();
    }

    @Test
    @DisplayName("Check a valid widraw")
    private void testWidrawSuccess() {
        assertEquals(20, account.balance);

        boolean result = account.withdraw(10);

        assertTrue(result);
        assertEquals(10, account.balance);
    }

    @Test
    @DisplayName("Check an invalid widraw")
    private void testWidrawFail() {
        assertEquals(20, account.balance);

        boolean result = account.withdraw(30);

        assertFalse(result);
        assertEquals(20, account.balance);
    }
}
