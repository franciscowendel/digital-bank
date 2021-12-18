from typing import List
from client import Client
from account import Account
from time import sleep


accounts: List[Account] = []


def menu():
    try:
        print('-------------------------------------------------------')
        print('-------------------------ATM---------------------------')
        print('-------------------------------------------------------')
        print()
        print('1 - CRIAR CONTA: ')
        print('2 - EFETUAR DEPÓSITO: ')
        print('3 - EFETUAR SAQUE: ')
        print('4 - EFETUAR TRANSFERÊNCIA: ')
        print('5 - LISTAR CONTAS: ')
        print('6 - SAIR: ')
        print()

        option = input()
        if option == '' or not option.isnumeric():
            print()
            print('ESCOLHA UMA OPÇÃO!')
            print()
            sleep(0.5)
            menu()
        else:
            option = int(option)
            if option > 6:
                print()
                print('APENAS AS ESCOLHAS APRESENTADAS!')
                print()
                sleep(0.5)
                menu()

        if option == 1:
            criar_conta()
        elif option == 2:
            depositar()
        elif option == 3:
            sacar()
        elif option == 4:
            transferir()
        elif option == 5:
            listar_contas()
        elif option == 6:
            print()
            print('FIM DA SESSÃO...')
            print()
            sleep(0.5)
            exit(1)
        else:
            print()
            print('ERROR...')
            print()
        sleep(0.5)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Errors {err} found...'


def criar_conta():
    try:
        print('-------------')
        print('CRIAR CONTA: ')
        print('-------------')
        print()
        name: str = input('NOME: ')
        if name == '' or name.isnumeric():
            print()
            print('DIGITE SEU NOME!')
            print()
            sleep(0.5)
            menu()

        last_name: str = input('SOBRENOME: ')
        if last_name == '' or last_name.isnumeric():
            print()
            print('DIGITE SEU SOBRENOME!')
            print()
            sleep(0.5)
            menu()

        email: str = input('EMAIL: ')
        if email == '' or email.isnumeric():
            print()
            print('DIGITE SEU EMAIL!')
            print()
            sleep(0.5)
            menu()
        cpf: str = input('CPF: ')
        if cpf == '':
            print()
            print('DIGITE SEU CPF!')
            print()
            sleep(0.5)
            menu()

        data_nascimento: str = input('DATA DE NASCIMENTO: ')
        if data_nascimento == '':
            print()
            print('DIGITE SUA DATA DE NASCIMENTO!')
            print()
            sleep(0.5)
            menu()
        print()
        cliente: Client = Client(name, last_name, email, cpf, data_nascimento)

        conta: Account = Account(cliente)

        print('-------------------------')
        print('CONTA CRIADA COM SUCESSO!')
        print('-------------------------')
        print()
        sleep(0.5)
        accounts.append(conta)
        print('----------------')
        print('DADOS DA CONTA: ')
        print('----------------')
        print()
        print(conta)
        print()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Errors {err} found...'


def depositar():
    try:
        if len(accounts) > 0:
            print('----------------------------------------------------')
            print('DIGITE O NÚMERO DA CONTA QUE VAI RECEBER O DEPÓSITO:')
            print('----------------------------------------------------')
            print()
            for conta in accounts:
                print('------------------------------------------------')
                print(conta)
                print('------------------------------------------------')
                print()
            number = input()
            if number == '' or not number.isnumeric():
                print()
                print('DIGITE O NÚMERO!')
                print()
                sleep(0.5)
                menu()
            else:
                number = int(number)

            conta: Account = rastrear_conta(number)

            if conta:
                valor = input('DIGITE O VALOR DO DEPÓSITO: ')
                if valor == '' or not valor.isnumeric():
                    print()
                    print('DIGITE O VALOR DO DEPÓSITO!')
                    print()
                    sleep(0.5)
                    menu()
                else:
                    valor = int(valor)
                        
                conta.depositar(valor)

            else:
                print()
                print('CONTA NÃO ENCONTRADA!')
                print()
            sleep(0.5)
            menu()

        else:
            print()
            print('NENHUMA CONTA CRIADA!')
            print()
        sleep(0.5)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Errors {err} found...'


def sacar():
    try:
        if len(accounts) > 0:
            print('--------------------------------------------------')
            print('DIGITE O NÚMERO DA CONTA QUE VAI EFETUAR O SAQUE: ')
            print('--------------------------------------------------')
            print()
            for conta in accounts:
                print('----------------------------------------------')
                print(conta)
                print('----------------------------------------------')
                print()
            number = input()
            if number == '' or not number.isnumeric():
                print()
                print('DIGITE O NÚMERO DA CONTA!')
                print()
                sleep(0.5)
                menu()
            else:
                number = int(number)

            conta: Account = rastrear_conta(number)

            if conta:
                valor = input('DIGITE O VALOR DO SAQUE: ')
                if valor == '' or not valor.isnumeric():
                    print()
                    print('DIGITE O VALOR DO SAQUE!')
                    print()
                    sleep(0.5)
                    menu()
                else:
                    valor = float(valor)

                conta.sacar(valor)

            else:
                print()
                print('CONTA NÃO ENCONTRADA!')
                print()
                sleep(0.5)
                menu()

        else:
            print()
            print('NENHUMA CONTA CRIADA!')
            print()
        sleep(0.5)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Errors {err} found...'


def transferir():
    try:
        if len(accounts) > 0:

            print('---------------------------------------------------')
            print('DIGITE O NÚMERO DA CONTA QUE VAI FAZER O DEPÓSITO: ')
            print('---------------------------------------------------')
            print()
            for conta in accounts:
                print('-----------------------------------------------')
                print(conta)
                print('-----------------------------------------------')
                print()
            number_1 = input()
            if number_1 == '' or not number_1.isnumeric():
                print()
                print('DIGITE O NÚMERO DA CONTA!')
                print()
                sleep(0.5)
                menu()
            else:
                number_1 = int(number_1)

            conta_1 = rastrear_conta(number_1)

            if conta_1:
                print('-----------------------------------------------------')
                print('DIGITE O NÚMERO DA CONTA QUE VAI RECEBER O DEPÓSITO: ')
                print('-----------------------------------------------------')
                print()
                number_2 = input()
                if number_2 == '' or not number_2.isnumeric():
                    print()
                    print('DIGITE O NÚMERO DA CONTA!')
                    print()
                    sleep(0.5)
                    menu()
                else:
                    number_2 = int(number_2)

                conta_2 = rastrear_conta(number_2)

                if conta_2:
                    valor = input('DIGITE O VALOR DA TRANSFERÊNCIA: ')
                    if valor == '' or not valor.isnumeric():
                        print()
                        print('DIGITE O VALOR DA TRANSFERÊNCIA!')
                        print()
                        sleep(0.5)
                        menu()
                    else:
                        valor = float(valor)

                    conta_1.transferir(conta_2, valor)

            else:
                print()
                print('CONTA NÃO ENCONTRADA!')
                print()
                sleep(0.5)
                menu()
        else:
            print()
            print('NENHUMA CONTA CRIADA!')
            print()
        sleep(0.5)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Errors {err} found...'


def listar_contas():
    if len(accounts) > 0:

        print('-----------------')
        print('LISTA DE CONTAS: ')
        print('-----------------')
        print()
        for conta in accounts:
            print('-------------------------------------------')
            print(conta)
            print('-------------------------------------------')
            print()
    else:
        print()
        print('NENHUMA CONTA CRIADA!')
        print()
    sleep(0.5)
    menu()


def rastrear_conta(number):
    x = None

    if len(accounts) > 0:
        for conta in accounts:
            if conta.numero == number:
                x = conta
    return x


if __name__ == '__main__':
    menu()
