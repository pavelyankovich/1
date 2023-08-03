import random
import string
import json
from features.steps import global_params as GP
import webcolors


def parse_tabel(tabel):
    params = {}
    for item in tabel:
        params.setdefault(f'{item[0]}', f'{item[1]}')

    GP.TABLE = params
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
        case 'doRegister':
            url = 'http://users.bugred.ru/tasks/rest/doregister'
        case 'CreateCompany':
            url = 'http://users.bugred.ru/tasks/rest/createcompany'
        case 'UpdateItem':
            url = 'http://shop.bugred.ru/api/items/update/'
        case 'UploadPhoto':
            url = GP.URL + 'api/items/upload_photo/'

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

def update_item(values=None):
    data = """
    {
    "id": "",
    "name": "",
    "section": "",
    "description": ""
    }"""
    request_body = json.loads(data)
    if values:
        request_body.update(values)
    request_body["id"] = int(GP.ID)
    GP.NAME = f'test_{generate_random_string(5)}'
    GP.CURRENT_SECTION = random.choice(GP.SECTION_LIST)
    GP.DESCRIPTION = f'{generate_random_string(25)}'
    request_body["name"] = GP.NAME
    request_body["section"] = GP.CURRENT_SECTION
    request_body["description"] = GP.DESCRIPTION
    GP.DICT = request_body
    return request_body

def date_create_item(values=None):
    date = """
        {
        "name": "",
        "section": "",
        "description": ""
        }"""
    body = json.loads(date)
    if values:
        body.update(values)

    GP.NAME = f"test_{generate_random_string(5)}"
    GP.CURRENT_SECTION = f'{random.choice(GP.SECTION)}'
    GP.DESCRIPTION = f"{generate_random_string(5)} {generate_random_string(5)}"

    body['name']        = GP.NAME
    body['section']     = GP.CURRENT_SECTION
    body['description'] = GP.DESCRIPTION

    return body

def upload_photo(photo):





def comparing_colors(color_css,color_word):
    color_word = webcolors.name_to_hex(color_word)
    print(color_word)
    print(color_css)