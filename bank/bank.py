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
        print('1 - CRIAR CONTA: ')
        print('2 - EFETUAR DEPÓSITO: ')
        print('3 - EFETUAR SAQUE: ')
        print('4 - EFETUAR TRANSFERÊNCIA: ')
        print('5 - LISTAR CONTAS: ')
        print('5 - SAIR: ')
        print()

        opcao: int = int(input())

        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            efetuar_deposito()
        elif opcao == 3:
            efetuar_saque()
        elif opcao == 4:
            efetuar_transferencia()
        elif opcao == 5:
            listar_contas()
        elif opcao == 6:
            print('CONEXÃO TERMINADA...')
            sleep(1)
            exit(1)

        else:
            print('OPÇÃO INVÁLIDA!')
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def criar_conta():
    try:
        print('-------------')
        print('CRIAR CONTA: ')
        print('-------------')
        print()
        nome: str = input('NOME: ')
        if nome == '':
            exit(1)
        sobrenome: str = input('SOBRENOME: ')
        if sobrenome == '':
            exit(1)
        email: str = input('EMAIL: ')
        if email == '':
            exit(1)
        cpf: str = input('CPF: ')
        if cpf == '':
            exit(1)
        data_nascimento: str = input('DATA DE NASCIMENTO: (dd/mm/yyyy) ')
        if data_nascimento == '':
            exit(1)
        print()

        cliente: Client = Client(nome, sobrenome, email, cpf, data_nascimento)

        conta: Account = Account(cliente)

        print('-------------------------')
        print('CONTA CRIADA COM SUCESSO!')
        print('-------------------------')
        print()
        sleep(2)
        contas.append(conta)
        print('----------------')
        print('DADOS DA CONTA: ')
        print('----------------')
        print()
        print(conta)
        print()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def efetuar_deposito():
    try:
        if len(contas) > 0:

            print('-----------------------------------------------------')
            print('DIGITE O CÓDIGO DA CONTA QUE VAI RECEBER O DEPÓSITO: ')
            print('-----------------------------------------------------')
            print()
            for conta in contas:
                print(conta)
                print('------------------------')
                print()
            numero: int = int(input())

            conta: Account = rastrear_conta(numero)

        else:
            print('NENHUMA CONTA CRIADA...')
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def efetuar_saque():
    pass


def efetuar_transferencia():
    pass


def listar_contas():
    pass


def rastrear_conta(numero):
    x: Account = None  # noqa

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                x: Account = conta
    return x


if __name__ == '__main__':
    menu()
