from datetime import datetime
from datetime import date


def float_to_str(value) -> str:
    """Transforms a float value into a string."""
    return f'R$ {value:,.2f}'


def date_to_str(data) -> str:
    """Transforms a date object into a string."""
    return data.strftime('%d/%m/%Y')


def str_to_date(data) -> date:
    """Tranforms a string into a date object."""
    return datetime.strptime(data, '%d/%m/%Y')
