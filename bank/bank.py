from typing import List
from account import Account
from client import Client
from time import sleep


contas: List[Account] = []


def menu():
    """Mostra as opções do banco digital para o usuário."""
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
        print('6 - SAIR: ')
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
    """Cria uma conta para o usuário após informado alguns dados."""
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
    """Deposita o valor informado na conta caso o número desta exista."""
    try:
        if len(contas) > 0:

            print('-----------------------------------------------------')
            print('DIGITE O NÚMERO DA CONTA QUE VAI RECEBER O DEPÓSITO: ')
            print('-----------------------------------------------------')
            print()
            for conta in contas:
                print(conta)
                print('------------------------')
                print()
            numero: int = int(input())

            conta: Account = rastrear_conta(numero)

            if conta:
                valor: float = float(input('INFORME O VALOR DO DEPÓSITO: '))

                conta.depositar(valor)

            else:
                print('CONTA COM O NÚMERO INFORMADO NÃO FOI ENCONTRADA!')

        else:
            print('NENHUMA CONTA CRIADA...')
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def efetuar_saque():
    """Efetua o saque na conta informada caso o número desta exista."""
    try:
        if len(contas) > 0:

            print('------------------------------------------------')
            print('DIGITE O NÚMERO DA CONTA QUE VAI FAZER O SAQUE: ')
            print('------------------------------------------------')
            print()
            for conta in contas:
                print(conta)
                print('------------------------')
                print()
            numero: int = int(input())

            conta: Account = rastrear_conta(numero)

            if conta:
                valor: float = float(input('INFORME O VALOR DO SAQUE: '))

                conta.sacar(valor)

            else:
                print('CONTA COM O NÚMERO INFORMADO NÃO FOI ENCONTRADA!')

        else:
            print('NENHUMA CONTA CRIADA...')
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def efetuar_transferencia():
    """Transfere de uma conta para a outra (caso o número destas existam) o valor informado."""
    try:
        if len(contas) > 0:

            print('---------------------------------------------------')
            print('DIGITE O NÚMERO DA CONTA QUE VAI FAZER O DEPÓSITO: ')
            print('---------------------------------------------------')
            print()
            for conta in contas:
                print(conta)
                print('------------------------')
                print()
            numero_origem: int = int(input())

            conta_origem: Account = rastrear_conta(numero_origem)

            if conta_origem:
                print('-----------------------------------------------------')
                print('DIGITE O NÚMERO DA CONTA QUE VAI RECEBER O DEPÓSITO: ')
                print('-----------------------------------------------------')
                print()

                numero_destino: int = int(input())

                conta_destino: Account = rastrear_conta(numero_destino)

                if conta_destino:

                    valor: float = float(input('INFORME O VALOR DA TRANSFERÊNCIA: '))

                    conta_origem.transferir(conta_destino, valor)

                else:
                    print('NÚMERO DA CONTA NÃO FOI ENCONTRADO...')
                sleep(1)
                menu()

            else:
                print('CONTA COM O NÚMERO INFORMADO NÃO FOI ENCONTRADA!')
            sleep(1)
            menu()

        else:
            print('NENHUMA CONTA CRIADA...')
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def listar_contas():
    """Lista todas as contas criadas."""
    if len(contas) > 0:

        print('-----------------')
        print('LISTA DE CONTAS: ')
        print('-----------------')
        print()
        for conta in contas:
            print(conta)
            print('----------------')
            print()

    else:
        print('NENHUMA CONTA CRIADA!')
    sleep(1)
    menu()


def rastrear_conta(numero):
    """Dá a possibilidade de pegarmos uma conta pelo seu número."""
    x: Account = None  # noqa

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                x: Account = conta
    return x


if __name__ == '__main__':
    menu()
