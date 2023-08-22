import json
import time
import requests
import help_file_rest as HPR
import features.steps.global_params as GP
import features.params.xpath_helper as XP
import features.params.rand_value as RV
import re
import colorama


from behave import step
from selenium.webdriver.common.by import By

colorama.init(autoreset=True)

def open(context, *args):
  pass


@step('Я захожу на страничку "{name}"')
def step_impl(context,name):
    url = HPR.full_url(name)
    context.driver.get(url)
    time.sleep(1)


@step('Ввожу в поле c email "{email}" и нажимаю кнопку "{value}"')
def step_impl(context, email, value):
    element = context.driver.find_element(By.XPATH, f"//tr/td[contains(text(),'{email}')]/..//a[text()='{value}']")
    element.click()
    time.sleep(5)

@step('Создаю товар через "{api}"')
def step_impl(context, api):

    if api == 'rest':
        tabel = HPR.parse_tabel(context.table)
        body = HPR.date_create_item(tabel)
        url = HPR.http_metods("CreateItem")
        GP.RESPONSE = requests.post(url, body)
    # elif api == 'soap':





@step('Проверяем работу метода "{metod}"')
def step_impl(context, metod):

    if context.table:
        tabel = HPR.parse_tabel(context.table)
    else:
        pass

    if metod == "CreateItem":
        body = HPR.date_create_item(tabel)
    elif metod == "UpdateItem":
        body = HPR.update_item(tabel)
    elif metod == "UploadPhoto":
        photo, body = HPR.form_request_body_for_upload()

    url = HPR.http_metods(metod)

    if metod == "UploadPhoto":
        response = requests.post(url, data = body, files = photo)
    else:
        response = requests.post(url, body)

    GP.DICT = response.json()

    if metod == 'CreateItem':
        GP.ID = (GP.DICT['result']['id'])
        GP.NAME = (GP.DICT['result']['name'])

    # проверка результатов
    HPR.show_messege(response)
@step('Я ищу пользователя со значениями')
def step_impl(context,):
    tabel = HPR.parse_tabel(context.table)
    tabell = HPR.glob_params_tabel(tabel)
    print(tabell)
    val1 = HPR.glob_params(tabell['email'])
    val2 = HPR.glob_params(tabell['name'])
    xpath = f"//tr/td[contains(text(),'{val1}')]/../td[contains(text(),'{val2}')]/../td/a[contains(text(),'Посмотреть')]"
    element = context.driver.find_element(By.XPATH,xpath)
    element.click()
    time.sleep(10)

@step('Я захожу на страничку товара с id "{id}"')
def step_impl(context,id):
    item = HPR.glob_params(id)
    full_url = f"{GP.URL}shop/item/{item}"
    context.driver.get(full_url)
    print(GP.ID)
    time.sleep(5)

@step('Нахожу ссылку в параметрах товара')
def step_impl(context):
    xpath = XP.xpath_parser('xpath_param_item')
    val = 'Параметры'
    text = context.driver.find_element(By.XPATH, xpath % str(val))
    print(text.text)
    link = re.search('http\S+', text.text)
    if link:
        print(f'В параметрах товара найдена ссылка {link[0]}')
    else:
        raise ValueError(f'В параметрах товара ссылки - нет')
    # print(link)


@step('Проверка обновленного товара')
def step_impl(context):
    item_name = context.driver.find_element(By.XPATH, XP.xpath_parser('item_name')).text
    item_section = context.driver.find_element(By.XPATH, XP.xpath_parser('item_section')).text
    item_size = context.driver.find_element(By.XPATH, XP.xpath_parser('item_size')).text
    item_size = re.search('[0-9]{2}', item_size)
    item_price = context.driver.find_element(By.XPATH, XP.xpath_parser('item_price')).text
    item_price = re.search('[0-9]*', item_price)

    item_color = context.driver.find_element(By.XPATH,XP.xpath_parser('item_color'))
    color = item_color.get_dom_attribute('style')
    color = color.split(':')[1]
    # print(GP.TABLE)


    # print(color)
    match item_name:
        case GP.NAME:
            print('Item name updated successfully!')
    match item_section:
        case GP.CURRENT_SECTION:
            print('Item section updated successfully!')
    if item_size[0] == GP.TABLE.get("size"):
        print('Item size updated successfully!')
    if item_price[0] == GP.TABLE.get("price"):
        print('Item price updated successfully!')

    print(GP.DICT.get("params"))

@step('Получаем данные о товаре "{id}"')
def step_impl(context, id):
    item = {
        'id' : f'{HPR.glob_params(id)}'
    }
    date = json.dumps(item)
    url = HPR.http_metods('Get')
    response = requests.post(url, date)
    GP.RESPONSE = response.json()
    print(GP.RESPONSE)

@step('Создаем "{numbers}" товара со следующими параметрами')
def step_impl(context, numbers):
    GP.TABLE = HPR.parse_tabel(context.table)
    item = HPR.glob_params_tabel(GP.TABLE)
    body = json.dumps(item, indent= 4)
    GP.NAME = item['name']
    url = HPR.http_metods('CreateItem')
    for num in range(int(numbers)):
        response = requests.post(url, body)
        GP.RESPONSES.append(response.json()['result'])

    HPR.show_messege(response)


@step('Находим все товары с названием "{name}"')
def step_impl(context, name):
    url = HPR.http_metods('Search')
    if name == 'RAND_NAME':
        name = GP.NAME

    body = {
        "query": name
    }
    response = requests.post(url, body)
    print(response.json()['result'])
    print(response.json())



@step('Удаляем товар с id "{id}"')
def step_impl(context, id):
    url = HPR.http_metods('Delete')
    if id == 'ID':
        id = GP.ID

    body = {
        "id": id
    }
    response = requests.post(url, body)
    if response.json()['status'] == 'ok':
        print(colorama.Fore.BLUE + f"{response.json()['result']}")
    elif response.json()['status'] == 'error':
        print(colorama.Fore.RED + f"{response.json()['message']}")

@step('Нажимаю на кнопку "{name}" в меню в верхней панели')
def step_impl(context, name):
    xpath = XP.xpath_parser('button_in_upper_panel')
    element = context.driver.find_element(By.XPATH, xpath % str(name))
    element.click()
    time.sleep(3)

@step('В поле c id "{name}" ввожу "{value}"')
def step_impl(context, name, value):
    value = HPR.glob_params(value)
    element = context.driver.find_element(By.ID,f"{name}")
    element.send_keys(value)
    time.sleep(1)

@step('Нажимаю на кнопку "{button}"')
def step_impl(context, button):
    xpath = XP.xpath_parser("button")
    element = context.driver.find_element(By.XPATH, xpath % str(button))
    element.click()
    time.sleep(2)

@step('В окне ожидаю увидеть сообщение "{exp_message}"')
def step_impl(context, exp_message):
    message_xpath = XP.xpath_parser('message_in_window')
    message = context.driver.find_element(By.XPATH, message_xpath % exp_message)
    print(colorama.Fore.GREEN + f"Окошко с сообщением '{message.text}' - найдено")


@step('Нажимаю на кнопку "{name}" в выпадающем списке')
def step_impl(context, name):
    xpath = XP.xpath_parser('button_in_dropdown')
    element = context.driver.find_element(By.XPATH, xpath % str(name))
    element.click()
    time.sleep(3)


@step('В поле c id "{line}" ожидаю увидеть текст - "{text}"')
def step_impl(context, line, text):
    text = HPR.glob_params(text)
    element = context.driver.find_element(By.ID, f"{line}")
    if element.get_attribute("value") == text:
        print(colorama.Fore.GREEN + f"Поле с текстом '{text}' - найдено")
    else:
        print(colorama.Fore.RED + f"Поле с текстом '{text}' -  не найдено, а найдено - {element.text}")

    time.sleep(1)

@step('Ввожу в поле "{line}" значение - "{value}"')
def step_impl(context, line, value):
    xpath = XP.xpath_parser('amount_item')
    element = context.driver.find_element(By.XPATH, xpath % str(line))
    element.send_keys(value)
    time.sleep(2)

@step('Нажимаем на значок корзины')
def step_impl(context):
    xpath = XP.xpath_parser('cart')
    element = context.driver.find_element(By.XPATH, xpath)
    element.click()
    time.sleep(2)


@step('Ожидаю что URL содержит - "{url}"')
def step_impl(context, url):

    if f'{url}' in context.driver.current_url:
        print(colorama.Fore.GREEN + f"URL содержит значение - {url}")
    else:
        print(colorama.Fore.RED + f"Упс! Что то пошло не так!")

    time.sleep(1)

@step('Хочу найти в строке поиска товар - "{name}"')
def step_impl(context, name):
    name = HPR.glob_params(name)
    xpath = XP.xpath_parser('search')
    element = context.driver.find_element(By.XPATH, xpath)
    element.send_keys(name)
    button = XP.xpath_parser('search_button')
    search_button = context.driver.find_element(By.XPATH, button)
    search_button.click()
    time.sleep(2)

@step('Ожидаю увидеть товаров на странице - "{value}"')
def step_impl(context, value):
    xpath = XP.xpath_parser('item_row')
    element = context.driver.find_elements(By.XPATH, xpath)
    if len(element) == int(value):
        print(colorama.Fore.GREEN + f"Количество найденных элементов совпадает с ожиданием!")
    else:
        print(colorama.Fore.RED + f"Упс! Количество найденных элементов = {len(element)}, а ожидали {int(value)}")
