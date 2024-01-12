from datetime import datetime
from datetime import date


def float_to_str(valor) -> str:
    return f'R$ {valor:,.2f}'


def date_to_str(data) -> str:
    return data.strftime('%d/%m/%Y')


def str_to_date(data) -> date:
    return datetime.strptime(data, '%d/%m/%Y')
