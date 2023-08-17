

 Feature: Регистрация нового пользователя

    Scenario: Регистрация нового пользователя
      Given Я захожу на страничку "Главная"
      Then Нажимаю на кнопку "Регистрация" в меню в верхней панели

      Then В поле c id "exampleInputName" ввожу "Павел"
      Then В поле c id "exampleInputEmail1" ввожу "RAND_EMAIL"
      Then В поле c id "exampleInputPassword1" ввожу "123123"
      Then В поле c id "exampleInputPassword2" ввожу "123123"
      Then Нажимаю на кнопку "Зарегистрироваться"
      Then В окне ожидаю увидеть сообщение "Теперь вы можете войти используя свой email и пароль!"