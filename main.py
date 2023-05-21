from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("./drivers/chromedriver.exe")

def selector(path):
    element = driver.find_element(By.XPATH, f"{path}")
    print(element)
    assert element



def main():
    driver.get('https://ya.ru/')
    selector('//input[contains(@class, "search3__input mini-suggest__input")]')


if __name__=="__main__":
    main()

