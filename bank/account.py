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

    @saldo.setter
    def balance(self, value):
        self.__balance = value

    @property
    def extra_limit(self) -> float:
        return self.__extra_limit

    @limite_extra.setter
    def extra_limit(self, value):
        self.__extra_limit = value

    @property
    def total_balance(self) -> float:
        return self.__total_balance

    @saldo_total.setter
    def total_balance(self, value):
        self.__total_balance = value

    def _calculate_total_balance(self) -> float:
        return self.__balance + self.__extra_limit

    def __str__(self) -> str:
        return f"{self.client}" \
               f"\nAccount's code: {self.code}" \
               f"\nTotal balance: {float_to_str(self.total_balance)}"

    def depositar(self, value):
        """Deposita o valor informado pelo usuário na conta informada por este."""
        if value > 0:
            self.saldo = self.saldo + value
            self.saldo_total = self._calcula_saldo_total()
            print()
            print('DEPÓSITO FEITO COM SUCESSO!')
            print()
        else:
            print('ERROR...')

    def sacar(self, value):
        """Saca o valor informado pelo usuário da conta informada por este."""
        if 0 < value <= self.saldo_total:
            if self.saldo >= value:
                self.saldo = self.saldo - value
                self.saldo_total = self._calcula_saldo_total()

            else:
                resto: float = self.saldo - value
                self.limite_extra: float = self.limite_extra + resto
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total()
            print()
            print('SAQUE EFETUADO COM SUCESSO!')
            print()
        else:
            print('ERROR...')

    def transferir(self, other_account, value):
        """Transfere um valor de uma conta para outra após ser informado o código da conta origem e
        o código da conta destino."""
        if 0 < value <= self.saldo_total:
            if self.saldo >= value:
                self.saldo = self.saldo - value
                self.saldo_total = self._calcula_saldo_total()
                other_account.saldo = other_account.saldo + value
                other_account.saldo_total = other_account._calcula_saldo_total()  # noqa

            else:
                resto: float = self.saldo - value
                self.limite_extra = self.limite_extra + resto
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total()
                other_account.saldo = other_account.saldo + value
                other_account.saldo_total = other_account._calcula_saldo_total()  # noqa
            print()
            print('TRANSFERÊNCIA EFETUADA COM SUCESSO!')
            print()
        else:
            print('ERROR...')
