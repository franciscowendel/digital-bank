from aux import date_to_str, str_to_date
from datetime import date


class Client:

    contador = 100

    def __init__(self, name: str, last_name: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__code: int = Client.contador
        self.__name: str = name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_to_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Client.contador += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_nascimento_ed(self) -> str:
        return date_to_str(self.__data_nascimento)

    @property
    def data_cadastro_ed(self) -> str:
        return date_to_str(self.__data_cadastro)

    def __str__(self) -> str:
        return f"Client's code: {self.code}\nCLient's name: {self.name}\nClient's last name: {self.last_name}" \
               f"\nClient's email: {self.email}\nClient's cpf: {self.cpf}"\
               f"\nClient's birthday: {self.data_nascimento_ed}" \
               f"\nClient's day of registration: {self.data_cadastro_ed}"
