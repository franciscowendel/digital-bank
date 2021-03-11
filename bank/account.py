from client import Client
from aux import float_to_str


class Account:

    codigo: int = 1000

    def __init__(self, cliente: Client) -> None:
        self.__numero: int = Account.codigo
        self.__cliente: Client = cliente
        self.__saldo: float = 0.0
        self.__limite_extra: float = 100.00
        self.__saldo_total: float = self._calcula_saldo_total
        Account.codigo += 1

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cliente(self) -> Client:
        return self.__cliente

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def limite_extra(self) -> float:
        return self.__limite_extra

    @limite_extra.setter
    def limite_extra(self, valor):
        self.__limite_extra = valor

    @property
    def saldo_total(self) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self, valor):
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self):
        return self.__saldo + self.__limite_extra

    def __str__(self):
        return f'Número da conta: {self.numero}\nDados do cliente: {self.cliente}' \
               f'\nSaldo total: {float_to_str(self.saldo_total)}'

    def depositar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print('DEPÓSITO FEITO COM SUCESSO!')
        else:
            print('VALOR DE DEPÓSITO MENOR QUE ZERO!')

    def sacar(self, valor):
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total

            else:
                resto: float = self.saldo - valor
                self.limite_extra = self.limite_extra + resto
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('SAQUE EFETUADO COM SUCESSO!')

        else:
            print('VALOR DE SAQUE MENOR QUE ZERO!')

    def transferir(self, conta_destino, valor):
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                conta_destino.saldo = conta_destino.saldo + valor
                conta_destino.saldo_total = conta_destino._calcula_saldo_total  # noqa

            else:
                pass
        else:
            print('ERRO AO EFETUAR A TRANSFERÊNCIA!')
