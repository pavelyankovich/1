
  Feature: Поиск товара в базе данных
   Scenario: Поиск товара в базе данных по названию
      Given Проверяем работу метода "CreateItem":
        | key    | value                                                                                                                                                                                                      |
        | color  | RED                                                                                                                                                                                                        |
        | size   | 20                                                                                                                                                                                                         |
        | price  | 200                                                                                                                                                                                                        |
        | params | Добро пожаловать в наш магазин, подробности на сайте https://vc.ru/s/1597527-python/637482-nachalnoe-rukovodstvo-po-python-dlya-nachinayushchih-programmistov-obzor-sintaksisa-bazovye-funkcii-i-operatory рады вас видеть |

     Then Нахожу в БД все данные о товаре с именем - "NAME"