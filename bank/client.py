from auxiliary import (
    date_to_str, 
    str_to_date
)

from datetime import date


class Client:

    number: int = 1

    def __init__(self, name: str, last_name: str, email: str, cpf: str, birthday: str) -> None:
        self.__code: int = Client.number
        self.__name: str = name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birthday: date = str_to_date(birthday)
        self.__day_of_registration: date = date.today()
        Client.number += 1

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
    def birthday_edited(self) -> str:
        return date_to_str(self.__birthday)

    @property
    def day_of_registration_edited(self) -> str:
        return date_to_str(self.__day_of_registration)

    def __str__(self) -> str:
        return f"Client's code: {self.code}\nCLient's name: {self.name}\nClient's last name: {self.last_name}" \
               f"\nClient's email: {self.email}\nClient's cpf: {self.cpf}"\
               f"\nClient's birthday: {self.birthday_edited}" \
               f"\nClient's day of registration: {self.day_of_registration_edited}"
