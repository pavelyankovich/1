import time

from selenium import webdriver


def before_feature(context, feature):
    print("Тест начался")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_feature(context, feature):
    context.driver.quit()
    time.sleep(2)