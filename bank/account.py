from aux import float_to_str
from client import Client


class Account:

    codigo: int = 1000

    def __init__(self, client: Client) -> None:
        self.__numero: int = Account.codigo
        self.__client: Client = client
        self.__saldo: float = 0.0
        self.__limite_extra: float = 100.00
        self.__saldo_total: float = self._calcula_saldo_total()
        Account.codigo += 1

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def client(self):
        return self.__client

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    @property
    def limite_extra(self) -> float:
        return self.__limite_extra

    @limite_extra.setter
    def limite_extra(self, value):
        self.__limite_extra = value

    @property
    def saldo_total(self) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor):
        self.__saldo_total = valor

    def _calcula_saldo_total(self) -> float:
        return self.__saldo + self.__limite_extra

    def __str__(self) -> str:
        return f"Account's number: {self.numero}\n{self.client}" \
               f"\nTotal balance: {float_to_str(self.saldo_total)}"

    def depositar(self, value):
        """Deposita o valor informado pelo usuário na conta informada por este."""
        if value > 0:
            self.saldo = self.saldo + value
            self.saldo_total = self._calcula_saldo_total
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
                self.saldo_total = self._calcula_saldo_total

            else:
                resto: float = self.saldo - value
                self.limite_extra: float = self.limite_extra + resto
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
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
