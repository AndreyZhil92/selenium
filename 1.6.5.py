'''Попробуем реализовать один из автотестов из предыдущего шага. Вам дана страница с
формой регистрации. Проверьте, что можно зарегистрироваться на сайте, заполнив только
обязательные поля, отмеченные символом *: First name, last name, email. Текст для полей
может быть любым. Успешность регистрации проверяется сравнением ожидаемого текста
"Congratulations! You have successfully registered!" с текстом на странице, которая
открывается после регистрации. Для сравнения воспользуемся стандартной конструкцией assert
из языка Python.
Ниже дан шаблон кода, который вам нужно использовать для своего теста. Не забывайте, что селекторы должны
быть уникальными.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.CLASS_NAME, "form-control.first").send_keys("Andrey")
    time.sleep(1)
    input2 = browser.find_elements_by_xpath('/html/body/div[1]/form/div[1]/div[2]/input').click().send_keys("Zhilin")
    time.sleep(3)
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("az@mail.ru")
    time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#Задание: уникальность селекторов
'''Это задание с так называемым пир-ревью: правильность вашего решения будут проверять другие учащиеся. 
Также и вам предстоит проверить чужой код. Ознакомившись с разными способами решения одной и той же 
задачи, вы сможете лучше понять изучаемую тему.

У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться 
на сайте. Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более 
современной. Обновленная страница доступна по другой ссылке. К сожалению, в процессе изменений они 
случайно внесли баг в форму регистрации.

Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. 
Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы 
и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. 
Пугаться не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте.

Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿

Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html'''
