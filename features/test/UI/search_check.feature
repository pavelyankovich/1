
Feature: Проверка работы поиска
   Scenario: Проверка работы поиска
     Given Проверяем работу метода "CreateItem":
        | key    | value                                                                                                                                                                                                      |
        | color  | RED                                                                                                                                                                                                        |
        | size   | 20                                                                                                                                                                                                         |
        | price  | 200                                                                                                                                                                                                        |
        | params | Добро пожаловать в наш магазин, подробности на сайте https://vc.ru/s/1597527-python/637482-nachalnoe-rukovodstvo-po-python-dlya-nachinayushchih-programmistov-obzor-sintaksisa-bazovye-funkcii-i-operatory рады вас видеть |

     Given Я захожу на страничку "Главная"
     Then Хочу найти в строке поиска товар - "NAME"
     Then Ожидаю увидеть товаров на странице - "1"
