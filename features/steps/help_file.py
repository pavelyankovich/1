import random
import string
import json
from features.steps import global_params as GP



def parse_tabel(tabel):
    params = {}
    for item in tabel:
        params.setdefault(f'{item[0]}', f'{item[1]}')
    return params

def glob_params_tabel(tabel):
    for k, v in tabel.items():
        if v == 'EMAIL':
            tabel[k] = GP.EMAIL
        elif v == 'NAME':
            tabel[k] = GP.NAME
        elif v == 'ID':
            tabel[k] = GP.ID

    return tabel

def glob_params(param):
    if param == 'EMAIL':
        param = GP.EMAIL
    elif param == 'ID':
        param = GP.ID

    return param






def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def http_metods(metod):
    url = None

    match metod:
        case "CreateItem":
            url = GP.URL + "api/items/create/"

    return url

def date_doregister():
    # заготовка данных
    date = """
       {
       "email": "email",
       "name": "name",
       "password": "password"
       }
       """
    body = json.loads(date)
    print(f'{GP.EMAIL} и {GP.NAME}')

    GP.EMAIL = f"{generate_random_string(10)}@test2.ru"
    GP.NAME = f"{generate_random_string(10)}"
    password = "123123"

    # вставляем рандомные значения в Json
    body['email'] = GP.EMAIL
    body['name'] = GP.NAME
    body['password'] = password

    return  body

def date_create_item(values=None):
    date = """
    {
    "name":"",
    "section":"",
    "description":""
    }
    """

    body = json.loads(date)
    if values:
        body.update(values)

    GP.NAME = f"test_{generate_random_string(5)}"
    GP.SECTION = f'{random.choice(GP.SECTION)}'
    GP.DESCRIPTION = f"{generate_random_string(5)} {generate_random_string(5)}"

    body['name']        = GP.NAME
    body['section']     = GP.SECTION
    body['description'] = GP.DESCRIPTION

    return body