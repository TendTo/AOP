import logging
import aspectlib
from Account import Account

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AccountAspect:
    WARN_BALANCE = 10

    @staticmethod
    @aspectlib.Aspect(bind=True)
    def log_on_before_account_withdraw(cutpoint, account: Account, *args, **kwargs):
        logger.info(f"Function signature: {cutpoint.__name__}")
        logger.info(f"List of arguments: {args} | Named arguments: {kwargs}")

        if account.balance <= AccountAspect.WARN_BALANCE:
            logger.warning(f"Attempt to widraw with low balance: current {account.balance}, warn set at {AccountAspect.WARN_BALANCE}")

        ret = yield aspectlib.Proceed
        yield aspectlib.Return(ret)

    @staticmethod
    @aspectlib.Aspect()
    def log_on_after_account_withdraw(account: Account, *args, **kwargs):
        ret = yield aspectlib.Proceed

        logger.info(f"Function return value: {ret}")
        if not ret:
            logger.warning(f"Attempt to widraw failed. | Current balance: {account.balance} | Amount requested: {args[0]}")

        yield aspectlib.Return(ret)

aspectlib.weave(Account, AccountAspect.log_on_before_account_withdraw, methods='withdraw')
aspectlib.weave(Account, AccountAspect.log_on_after_account_withdraw, methods='withdraw')

# Works too
# aspectlib.weave('Account.Account', AccountAspect.log_on_before_account_withdraw, methods='withdraw')
# aspectlib.weave('Account.Account', AccountAspect.log_on_after_account_withdraw, methods='withdraw')
