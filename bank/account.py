from client import Client
from aux import float_to_str


class Account:

    codigo: int = 1000

    def __init__(self, cliente: Client) -> None:
        self.__numero: int = Account.codigo
        self.__cliente: Client = cliente
        self.__saldo: float = 0.0
