import random
import string
import json
from features.steps import global_params as GP
import webcolors
import os
import colorama
from features.params import rand_value as RV
from bs4 import BeautifulSoup as BS



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
        elif v == 'RAND_NAME':
            tabel[k] = RV.RAND_NAME


    return tabel

def glob_params(param):
    match param:
        case 'EMAIL':
            param = GP.EMAIL
        case 'ID':
            param = GP.ID
        case 'TEST_EMAIL':
            param = GP.TEST_EMAIL
        case 'TEST_PASSWORD':
            param = GP.TEST_PASSWORD
        case 'RAND_EMAIL':
            param = RV.RAND_EMAIL
        case 'NAME':
            param = GP.NAME

    return param

def full_url(url):
    match url:
        case "Регистрация":
            url = GP.URL + "user/register/index"
        case "Главная":
            url = GP.URL
        case 'Вход':
            url = GP.URL + "user/login/index"

    return url





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
        case 'Search':
            url = GP.URL + "api/items/search/"
        case 'Get':
            url = GP.URL + "api/items/get"
        case 'Delete':
            url = GP.URL + "api/items/delete"

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

    GP.EMAIL = f"{RV.generate_random_string(10)}@test2.ru"
    GP.NAME = f"{RV.generate_random_string(10)}"
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
    GP.NAME = f'test_{RV.generate_random_string(5)}'
    GP.CURRENT_SECTION = random.choice(GP.SECTION_LIST)
    GP.DESCRIPTION = f'{RV.generate_random_string(25)}'
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

    GP.NAME = f"test_{RV.generate_random_string(5)}"
    GP.CURRENT_SECTION = f'{random.choice(GP.SECTION)}'
    GP.DESCRIPTION = f"{RV.generate_random_string(5)} {RV.generate_random_string(5)}"

    body['name']        = GP.NAME
    body['section']     = GP.CURRENT_SECTION
    body['description'] = GP.DESCRIPTION

    return body

def form_request_body_for_upload():
    image_dir = 'features/File/Photo'
    random_file = random.choice(os.listdir(image_dir))
    file = os.path.join(image_dir, random_file)

    photo = {
        'photo': open(file, 'rb')
    }
    data = {
        'id': GP.ID
    }
    return photo, data

def comparing_colors(color_css,color_word):
    color_word = webcolors.name_to_hex(color_word)
    print(color_word)
    print(color_css)

def show_messege(response):
    if response.status_code == 200:
        print(colorama.Fore.GREEN + f'Метод прошел успешно: code {response.status_code}')
        print(colorama.Fore.YELLOW + f'{response.json()}')
    else:
        raise ValueError(colorama.Fore.RED +f'Метод завершился с ошибкой: code {response.status_code}')


# def get_atribut_teg (xpath)