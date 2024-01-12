from auxiliary import float_to_str
from client import Client


class Account:

    number: int = 1

    def __init__(self, client: Client) -> None:
        self.__code: int = Account.number
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__extra_limit: float = 50.00
        self.__total_balance: float = self._calculate_total_balance()
        Account.number += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def client(self):
        return self.__client

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def extra_limit(self) -> float:
        return self.__extra_limit

    @extra_limit.setter
    def extra_limit(self, value):
        self.__extra_limit = value

    @property
    def total_balance(self) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self, value):
        self.__total_balance = value

    def _calculate_total_balance(self) -> float:
        """Calculates the total balance of the account including the extra limit."""
        return self.__balance + self.__extra_limit

    def __str__(self) -> str:
        return f"{self.client}" \
               f"\nAccount's code: {self.code}" \
               f"\nTotal balance: {float_to_str(self.total_balance)}"

    def deposit(self, value):
        """Deposits an amount into the user's account."""
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self._calculate_total_balance()
            print()
            print('Deposit made successfully!')
            print()
        else:
            print()
            print('Error...')
            print()
            
    def withdraw(self, value):
        """Withdraws value from a user's account."""
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance()

            else:
                x: float = self.balance - value
                self.extra_limit: float = self.extra_limit + x
                self.balance = 0
                self.total_balance = self._calculate_total_balance()
            print()
            print('Withdraw made successfully!')
            print()
        else:
            print()
            print('Error...')
            print()
            
    def transfer(self, other_account, value):
        """Transfers a value from an account to another."""
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance()
                other_account.balance = other_account.balance + value
                other_account.total_balance = other_account._calculate_total_balance()  # noqa

            else:
                x: float = self.balance - value
                self.extra_limit = self.extra_limit + x
                self.balance = 0
                self.total_balance = self._calculate_total_balance()
                other_account.balance = other_account.balance + value
                other_account.total_balance = other_account._calculate_total_balance()  # noqa
            print()
            print('Tranfer made successfully!')
            print()
        else:
            print()
            print('Error...')
            print()
            
