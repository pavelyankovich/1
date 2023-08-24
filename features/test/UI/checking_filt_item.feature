 Feature: Поиск товара в базе данных
   Scenario: Поиск товара в базе данных по названию
      Given Создаем "1" товара со следующими параметрами:
        | key         | value                    |
        | name        | RAND_NAME                |
        | section     | ＼(〇_ｏ)／                  |
        | description | Can't atomatize soap api |
        | color       | RED                      |
        | size        | 20                       |
        | price       | 200                      |
        | params      | Random merchandise       |

       Given Создаем "1" товара со следующими параметрами:
        | key         | value                    |
        | name        | RAND_NAME                |
        | section     | ＼(〇_ｏ)／                  |
        | description | Can't atomatize soap api |
        | color       | RED                      |
        | size        | 30                       |
        | price       | 200                      |
        | params      | Random merchandise       |


     Given Я захожу на страничку "＼(〇_ｏ)／"

     Then Нажимаю на чекбокс с названием - "RED"

     Then Ожидаю увидеть товаров на странице - "2"

     Then Удаляем товары с id "RESPONSES"