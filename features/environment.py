from selenium import webdriver


def before_feature(context, feature):
    print("asd")
    context.driver = webdriver.Chrome()


def after_feature(context, feature):
    context.driver.quit()