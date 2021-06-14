package com.tend.model;

import com.tend.Main;

public class Account {
    public int balance = 20;

    public boolean withdraw(int amount) {
        if (balance < amount) {
            System.out.println(Main.ANSI_YELLOW + "[ACTUAL FUNCTION] Not enough balance" + Main.ANSI_RESET);
            return false;
        }
        balance -= amount;
        System.out.println(Main.ANSI_YELLOW +  String.format("[ACTUAL FUNCTION] Widraw %s", amount + Main.ANSI_RESET));
        return true;
    }

    public boolean deposit(int amount) {
        balance += amount;
        return true;
    }
}