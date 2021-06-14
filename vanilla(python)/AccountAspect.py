import sys
import logging
import re
from typing import Union
from Account import Account

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AccountAspect:
    WARN_BALANCE = 10

    @staticmethod
    def log_on_before_account_withdraw(fn):

        def wrapper(account: Account, *args, **kwargs):

            logger.info(f"Function signature: {fn.__name__}")
            logger.info(f"List of arguments: {args} | Named arguments: {kwargs}")

            if account.balance <= AccountAspect.WARN_BALANCE:
                logger.warning(f"Attempt to widraw with low balance: current {account.balance}, warn set at {AccountAspect.WARN_BALANCE}")
            return fn(account, *args, **kwargs)

        return wrapper

    @staticmethod
    def log_on_after_account_withdraw(fn):

        def wrapper(account: Account, *args, **kwargs):
            ret = fn(account, *args, **kwargs)

            logger.info(f"Function return value: {ret}")
            if not ret:
                logger.warning(f"Attempt to widraw failed. | Current balance: {account.balance} | Amount requested: {args[0]}")
            return ret

        return wrapper


def get_class(classpath: str) -> type:
    module_name, class_name= re.findall(r"(.+)\.([^.]+)$", classpath)[0]
    __import__(module_name)
    module = sys.modules[module_name]
    for key in dir(module):
        if key == class_name:
            return getattr(module, key)


def add_aspect(target: Union[type, str, list], method: str, wrapper):
    if isinstance(target, (tuple, list)):
        for single in target:
            if isinstance(single, type):
                setattr(single, method, wrapper(getattr(single, method)))
            elif isinstance(single, str):
                single = get_class(single)
                setattr(single, method, wrapper(getattr(single, method)))
    elif isinstance(target, type):
        setattr(target, method, wrapper(getattr(target, method)))
    elif isinstance(target, str):
        target = get_class(target)
        setattr(target, method, wrapper(getattr(target, method)))


add_aspect('Account.Account', 'withdraw', AccountAspect.log_on_before_account_withdraw)
add_aspect('Account.Account', 'withdraw', AccountAspect.log_on_after_account_withdraw)

# This works too
# Account.withdraw = AccountAspect.log_on_before_account_withdraw(Account.withdraw)
# Account.withdraw = AccountAspect.log_on_after_account_withdraw(Account.withdraw)
