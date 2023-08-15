"""В данном файле находятся все xpath для проекта"""


def xpath_parser(xpath):
    result = ''
    match xpath:
        case "xpath_param_item":
           result = "//div/p[contains(text(),'%s')]"
        case 'item_name':
            result = "//h2"
        case 'item_section':
            result = "//li[@class='breadcrumb-item'][2]/a"
        case "item_size":
            result = "//p[2]"
        case 'item_price':
            result = "//span[@class='label label-primary']"
        case 'item_color':
            result = "//div//span[@class='label']"
        case 'button_in_upper_panel':
            result = "//div//li[contains(@class,'nav-item')]/a[contains(text(),'%s')]"
    return result

