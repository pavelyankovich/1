Feature: Яндекс

    Scenario Outline: Яндекс
      Given Проверяем работу метода "CreateItem":
        | key    | value                                                                                                                                                                                                      |
        | color  | RED                                                                                                                                                                                                        |
        | size   | 20                                                                                                                                                                                                         |
        | price  | 200                                                                                                                                                                                                        |
        | params | Добро пожаловать в наш магазин, подробности на сайте https://vc.ru/s/1597527-python/637482-nachalnoe-rukovodstvo-po-python-dlya-nachinayushchih-programmistov-obzor-sintaksisa-bazovye-funkcii-i-operatory рады вас видеть |

      Then Я захожу на страничку товара с id "ID"
      Then Нахожу ссылку в параметрах товара

      And Проверяем работу метода "UpdateItem":
        | key    | value                          |
        | color  | ORANGE                         |
        | size   | <size>                         |
        | price  | <price>                        |
        | params | Информация о товаре обновлена! |

      Then Я захожу на страничку товара с id "ID"

      Then Проверка обновленного товара

      Examples:
        | size | price |
        | 20   | 2000  |
        | 30   | 3000  |
        | 40   | 4000  |
        | 50   | 5000  |
