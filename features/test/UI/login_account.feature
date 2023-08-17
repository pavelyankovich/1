
 Feature: Проверка входа в аккаунт
   Scenario: Проверка входа в аккаунт
      Given Я захожу на страничку "Вход"
      Then В поле c id "exampleInputEmail1" ввожу "TEST_EMAIL"
      Then В поле c id "exampleInputPassword1" ввожу "TEST_PASSWORD"
      Then Нажимаю на кнопку "Войти"

     Then Нажимаю на кнопку "Test" в меню в верхней панели
     Then Нажимаю на кнопку "Настройки" в выпадающем списке

     Then В поле c id "exampleInputEmail1" ожидаю увидеть текст - "TEST_EMAIL"