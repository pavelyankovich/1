


  Feature: Яндекс

    Scenario: Яндекс
#      Given Я захожу на "users.bugred.ru"
#      Then Ввожу в поле c email "mail2@mail.ru" и нажимаю кнопку "Посмотреть"
      Given Проверяем работу метода "doRegister":
        | key   | val    |
        | email | laksdl |
        | name  | hlaksd |

      Given Я захожу на "users.bugred.ru"
      Then Я ищу пользователя со значениями:
        | key   | val   |
        | email | EMAIL |
        | name  | NAME  |




