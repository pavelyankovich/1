
 Feature: Проверка функционала покупки товара
   Scenario: Проверка функционала покупки товара
     Given Проверяем работу метода "CreateItem":
        | key    | value                                                                                                                                                                                                      |
        | color  | RED                                                                                                                                                                                                        |
        | size   | 20                                                                                                                                                                                                         |
        | price  | 200                                                                                                                                                                                                        |
        | params | Добро пожаловать в наш магазин, подробности на сайте https://vc.ru/s/1597527-python/637482-nachalnoe-rukovodstvo-po-python-dlya-nachinayushchih-programmistov-obzor-sintaksisa-bazovye-funkcii-i-operatory рады вас видеть |

     Then Я захожу на страничку товара с id "ID"
     Then Ввожу в поле "Количество" значение - "1"
     Then Нажимаю на кнопку "Добавить в корзину"
     Then Нажимаем на значок корзины

     And  В поле c id "InputPhone" ввожу "+79999999999"
     And  В поле c id "InputAddr" ввожу "город Смоленск - мочевой пузырь России"

     Then Нажимаю на кнопку "Оформить заказ"
     Then Ожидаю что URL содержит - "finish"