from typing import List
from client import Client
from account import Account
from time import sleep


accounts: List[Account] = []


def bank():
    try:
        print('-------------------------------------------------------')
        print('-------------------------ATM---------------------------')
        print('-------------------------------------------------------')
        print()
        print('1 - Create account: ')
        print('2 - Deposit: ')
        print('3 - Withdraw: ')
        print('4 - Transfer: ')
        print('5 - List accounts: ')
        print('6 - Quit: ')
        print()

        option = input()
        if option == '' or not option.isnumeric():
            print()
            print('Choose an option!')
            print()
            sleep(0.5)
            bank()
        else:
            option = int(option)
            if option > 6:
                print()
                print('Type one of the options that were given.')
                print()
                sleep(0.5)
                bank()

        if option == 1:
            create_account()
        elif option == 2:
            deposit()
        elif option == 3:
            withdraw()
        elif option == 4:
            transfer()
        elif option == 5:
            list_accounts()
        elif option == 6:
            print()
            print('...')
            print()
            sleep(0.5)
            exit(1)
        else:
            print()
            print('Error...')
            print()
        sleep(0.5)
        bank()

    except (ValueError, TypeError) as err:
        return f'Errors {err} found...'


def create_account():
    try:
        print('------------------')
        print('Account creation: ')
        print('------------------')
        print()
        name: str = input('Name: ')
        if name == '' or name.isnumeric():
            print()
            print('Type your name!')
            print()
            sleep(0.5)
            bank()

        last_name: str = input('Lastname: ')
        if last_name == '' or last_name.isnumeric():
            print()
            print('Type your last name!')
            print()
            sleep(0.5)
            bank()

        email: str = input('Email: ')
        if email == '' or email.isnumeric():
            print()
            print('Type your email!')
            print()
            sleep(0.5)
            bank()
        cpf: str = input('CPF: ')
        if cpf == '':
            print()
            print('Type your cpf!')
            print()
            sleep(0.5)
            bank()

        birthday: str = input('Birthday: (dd/mm/yyyy)')
        if birthday == '':
            print()
            print('Type your birthday!')
            print()
            sleep(0.5)
            bank()
        print()
        client: Client = Client(name, last_name, email, cpf, birthday)

        account: Account = Account(client)

        print('-----------------------------')
        print('Account created successfully!')
        print('-----------------------------')
        print()
        sleep(0.5)
        accounts.append(account)
        print('----------------')
        print("Account's info: ")
        print('----------------')
        print()
        print(account)
        print()
        sleep(0.5)
        bank()

    except (ValueError, TypeError) as err:
        return f'Errors {err} found...'


def deposit():
    try:
        if len(accounts) > 0:
            print('-------------------------------------------------------')
            print("Type the account's code that will receive the deposit: ")
            print('-------------------------------------------------------')
            print()
            for account in accounts:
                print('------------------------------------------------')
                print(account)
                print('------------------------------------------------')
                print()
            code = input()
            if code == '' or not code.isnumeric():
                print()
                print('Type the code!')
                print()
                sleep(0.5)
                bank()
            else:
                code = int(code)

            account: Account = get_account_by_code(code)

            if account:
                deposit_value = input('Type the deposit value: ')
                if deposit_value == '' or not deposit_value.isnumeric():
                    print()
                    print('Type the deposit value!')
                    print()
                    sleep(0.5)
                    bank()
                else:
                    deposit_value = float(deposit_value)
                        
                account.deposit(deposit_value)

            else:
                print()
                print('Account not found!')
                print()
            sleep(0.5)
            bank()

        else:
            print()
            print('Zero accounts created!')
            print()
        sleep(0.5)
        bank()

    except (ValueError, TypeError) as err:
        return f'Errors {err} found...'


def withdraw():
    try:
        if len(accounts) > 0:
            print('---------------------------------------------------------')
            print("Type the account's code you are going to withdraw from.: ")
            print('---------------------------------------------------------')
            print()
            for account in accounts:
                print('----------------------------------------------')
                print(account)
                print('----------------------------------------------')
                print()
            code = input()
            if code == '' or not code.isnumeric():
                print()
                print('Type the code!')
                print()
                sleep(0.5)
                bank()
            else:
                code = int(code)

            account: Account = get_account_by_code(code)

            if account:
                withdraw_value = input('Type the withdraw value ')
                if withdraw_value == '' or not withdraw_value.isnumeric():
                    print()
                    print('Type the withdraw value!')
                    print()
                    sleep(0.5)
                    bank()
                else:
                    withdraw_value = float(withdraw_value)

                account.withdraw(withdraw_value)

            else:
                print()
                print('Account not found!')
                print()
                sleep(0.5)
                bank()

        else:
            print()
            print('Zero accounts created!')
            print()
        sleep(0.5)
        bank()

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


def get_account_by_code(code):
    x = None

    if len(accounts) > 0:
        for account in accounts:
            if account.code == code:
                x = account
    return x


if __name__ == '__main__':
    bank()
