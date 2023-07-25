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
        elif v == 'DICT':
            tabel[k] = GP.DICT

    return tabel

def glob_params(param):
    if param == 'EMAIL':
        param = GP.EMAIL

    return param


def parse_val(val):
    result = None
    match val:
        case "body":
            res



def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def http_metods(metod):
    url = None

    match metod:
        case "doRegister":
            url = 'http://users.bugred.ru/tasks/rest/doregister'
        case "CreateCompany":
            url = 'http://users.bugred.ru/tasks/rest/createcompany'

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

def date_createcompany():
    date = """
    {
  "company_name": "Алкоголики и тунеядцы",
  "company_type": "ООО",
  "company_users": ["test_anna@gmail.com", "mrak20@list.ru"],
  "email_owner": "aa+1@mail.com"
    }
    """