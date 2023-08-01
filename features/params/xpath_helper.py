"""В данном файле находятся все xpath для проекта"""


def xpath_parser(xpath):
    result = ''
    match xpath:
        case "xpath_param_item":
           result = "//div/p[contains(text(),'%s')]"
    return result

