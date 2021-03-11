from client import Client
from aux import float_to_str


class Account:

    codigo: int = 1000

    def __init__(self, cliente: Client) -> None:
        self.__numero: int = Account.codigo
        self.__cliente: Client = cliente
        self.__saldo: float = 0.0
        self.__limite_extra: float = 100.00
        self.__saldo_total: float = self._calcula_saldo_total()
        Account.codigo += 1

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Client:
        return self.cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
