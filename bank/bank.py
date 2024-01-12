from typing import List
from client import Client
from account import Account
from time import sleep


accounts: List[Account] = []


def bank():
    """Shows the options the user can choose."""
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
    """Creates an account for the user."""
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
        cpf: str = input('CPF: ***.***.***-**')
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

    except (ValueError, TypeError) as err:
        return f'Errors {err} found...'


def transfer():
    try:
        if len(accounts) > 0:

            print('---------------------------------------------------')
            print("Type the account's code that will make the transfer")
            print('---------------------------------------------------')
            print()
            for account in accounts:
                print('-----------------------------------------------')
                print(account)
                print('-----------------------------------------------')
                print()
            code_1 = input()
            if code_1 == '' or not code_1.isnumeric():
                print()
                print('Type the code!')
                print()
                sleep(0.5)
                bank()
            else:
                code_1 = int(code_1)

            account_1 = get_account_by_code(code_1)

            if account_1:
                print('--------------------------------------------------------')
                print("Type the account's code that will receive the transfer: ")
                print('--------------------------------------------------------')
                print()
                code_2 = input()
                if code_2 == '' or not code_2.isnumeric():
                    print()
                    print('Type the code!')
                    print()
                    sleep(0.5)
                    bank()
                else:
                    code_2 = int(code_2)

                account_2 = get_account_by_code(code_2)

                if account_2:
                    transfer_value = input('Type the transfer value: ')
                    if transfer_value == '' or not transfer_value.isnumeric():
                        print()
                        print('Type the transfer value!')
                        print()
                        sleep(0.5)
                        bank()
                    else:
                        transfer_value = float(transfer_value)

                    account_1.transfer(account_2, transfer_value)
                    
                else:
                    print()
                    print('Account not found!')
                    print()
                sleep(0.5)
                bank()

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


def list_accounts():
    if len(accounts) > 0:

        print('------------------')
        print('List of accounts: ')
        print('------------------')
        print()
        for account in accounts:
            print('-------------------------------------------')
            print(account)
            print('-------------------------------------------')
            print()
    else:
        print()
        print('Zero accounts created!')
        print()
    sleep(0.5)
    bank()


def get_account_by_code(code):
    """Function made to get the right account in the functions 'deposit', 'withdraw', 'transfer'."""
    x = None

    if len(accounts) > 0:
        for account in accounts:
            if account.code == code:
                x = account
    return x


if __name__ == '__main__':
    bank()
