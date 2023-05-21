import time

from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By


def open(context, *args):
  pass


@step('Я захожу на "{url}"')
def step_impl(context, url):
    context.driver.get("https://" + url)
    time.sleep(1)


@step('Ввожу в поле "{value}"')
def step_impl(context, value):
    element = context.driver.find_element(By.CLASS_NAME, 'search3__input.mini-suggest__input')
    element.send_keys(value)
    time.sleep(3)
