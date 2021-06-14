package com.tend.aspect;

import java.util.Arrays;
import java.util.logging.Logger;

import com.tend.model.Account;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

@Aspect
public class AccountAspect {
    final int WARN_BALANCE = 10;

    /**
     * Pointcut which binds on the Account.widraw method
     */
    @Pointcut("execution(* com.tend.model.Account.withdraw(..))")
    public void onAccountWithdraw() {
    }

    /**
     * Called before the target function is exectuted. Does some simple logging and
     * access the object's values.
     * 
     * @param joinPoint
     */
    @Before("onAccountWithdraw() && this(account)")
    public void logOnBeforeAccountWithdraw(JoinPoint joinPoint, Account account) {
        Logger logger = Logger.getLogger(account.getClass().getName());

        logger.info(String.format("Function signature: %s", joinPoint.getSignature().toString()));
        logger.info(String.format("List of arguments: %s", Arrays.toString(joinPoint.getArgs())));

        if (account.balance <= WARN_BALANCE) {
            logger.warning(String.format("Attempt to widraw with low balance: current %d, warn set at %d",
                    account.balance, WARN_BALANCE));
        }
    }

    /**
     * Called after the target function is exectuted. Does some simple logging and
     * access the object's values.
     * 
     * @param joinPoint
     */
    @AfterReturning(pointcut = "onAccountWithdraw() && this(account)", returning = "ret")
    public void logOnAfterAccountWithdraw(JoinPoint joinPoint, Account account, Boolean ret) {
        Logger logger = Logger.getLogger(account.getClass().getName());

        logger.info(String.format("Function return value: %s", ret.toString()));

        if (!ret) {
            logger.warning(String.format("Attempt to widraw failed. | Current balance: %d | Amount requested: %d",
                    account.balance, joinPoint.getArgs()[0]));
        }
    }
}