from datetime import date
import json
from django.conf import settings
import requests
import logging


def is_feriado(date: date):
    logging.info(f"Fazendo uma requisição para BrasilAPI na data: {date}")
    if settings.TESTING == True:
        logging.info(f"Requisição não realizada, em modo teste!")
        if date.day == 25 and date.month == 12:
            return True
        return False
    ano = date.year
    retorno = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
    if not retorno.status_code == 200:
        logging.error(f"Algum erro aconteceu ao consultar BrasilAPI!")
        return False
        # raise ValueError("Problema ao buscar feriados nacionais!")
    feriados = json.loads(retorno.text)
    for feriado in feriados:
        data_as_str = feriado["date"]
        data = date.fromisoformat(data_as_str)
        if data == date:
            return True
    return False
