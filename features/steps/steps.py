import time
import requests
import help_file as HP
import features.steps.global_params as GP

from behave import step
from selenium.webdriver.common.by import By


def open(context, *args):
  pass


@step('Я захожу на "{url}"')
def step_impl(context, url):
    context.driver.get("http://" + url)
    time.sleep(1)


@step('Ввожу в поле c email "{email}" и нажимаю кнопку "{value}"')
def step_impl(context, email, value):
    element = context.driver.find_element(By.XPATH, f"//tr/td[contains(text(),'{email}')]/..//a[text()='{value}']")
    element.click()
    time.sleep(5)

@step('Проверяем работу метода "{metod}"')
def step_impl(context, metod):
    # tabel = HP.parse_tabel(context.table)
    # GP.DICT = HP.glob_params_tabel(tabel)
    # print(context.table[0])
    if metod == "doRegister":
        date = HP.date_doregister()
    elif metod == "CreateCompany":
        date = HP.date_createcompany()

    url = HP.http_metods(metod)

    response = requests.post(url, date)
    print(GP.DICT)
    print(response.json())

    assert  response.status_code == 200

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

