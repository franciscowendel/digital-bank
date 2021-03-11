from typing import List
from account import Account
from client import Client
from time import sleep


contas: List[Account] = []


def menu():
    try:
        print('-------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------- ATM ----------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print('O QUE DESEJA FAZER: ')
        print()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def criar_conta():
    pass


def efetuar_deposito():
    pass


def efetuar_saque():
    pass


def efetuar_transferencia():
    pass


def listar_contas():
    pass


def rastrear_conta(numero):
    pass


if __name__ == '__main__':
    menu()
