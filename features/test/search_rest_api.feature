
Feature: Проверяем работу rest api search

    Scenario: Проверяем работу rest api search
      Given Создаем "2" товара со следующими параметрами:
        | key         | value                                                                                                                                                                                                                      |
        | name        | RAND_NAME                                                                                                                                                                                                                |
        | section     | Платья                                                                                                                                                                                                                     |
        | description | Не могу сделать автоматизацию проверки soap api на этом сайте!                                                                                                                                                             |
        | color       | RED                                                                                                                                                                                                                        |
        | size        | 20                                                                                                                                                                                                                         |
        | price       | 200                                                                                                                                                                                                                        |
        | params      | Добро пожаловать в наш магазин, подробности на сайте https://vc.ru/s/1597527-python/637482-nachalnoe-rukovodstvo-po-python-dlya-nachinayushchih-programmistov-obzor-sintaksisa-bazovye-funkcii-i-operatory рады вас видеть |

      Then Находим все товары с названием "RAND_NAME"