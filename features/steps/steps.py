import time
import requests
import help_file as HP
import features.steps.global_params as GP
import features.params.xpath_helper as XP
import re

from behave import step
from selenium.webdriver.common.by import By




def open(context, *args):
  pass


@step('Я захожу на на стартовую страничку')
def step_impl(context):
    context.driver.get(GP.URL)
    time.sleep(1)


@step('Ввожу в поле c email "{email}" и нажимаю кнопку "{value}"')
def step_impl(context, email, value):
    element = context.driver.find_element(By.XPATH, f"//tr/td[contains(text(),'{email}')]/..//a[text()='{value}']")
    element.click()
    time.sleep(5)

@step('Проверяем работу метода "{metod}"')
def step_impl(context, metod):
    tabel = HP.parse_tabel(context.table)
    # GP.DICT = HP.glob_params_tabel(tabel)
    # print(context.table[0])

    if metod == "CreateItem":
        body = HP.date_create_item(tabel)
    elif metod == "UpdateItem":
        body = HP.update_item(tabel)
    elif metod == "UploadPhoto":
        body = HP.

    url = HP.http_metods(metod)

    response = requests.post(url, body)
    GP.DICT = response.json()
    print(GP.DICT)
    if metod == 'CreateItem':
        GP.ID = (GP.DICT['result']['id'])

@step('Я ищу пользователя со значениями')
def step_impl(context,):
    tabel = HP.parse_tabel(context.table)
    tabell = HP.glob_params_tabel(tabel)
    print(tabell)
    val1 = HP.glob_params(tabell['email'])
    val2 = HP.glob_params(tabell['name'])
    xpath = f"//tr/td[contains(text(),'{val1}')]/../td[contains(text(),'{val2}')]/../td/a[contains(text(),'Посмотреть')]"
    element = context.driver.find_element(By.XPATH,xpath)
    element.click()
    time.sleep(10)

@step('Я захожу на страничку товара с id "{id}"')
def step_impl(context,id):
    item = HP.glob_params(id)
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
    HP.comparing_colors(color,GP.TABLE['color'])

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