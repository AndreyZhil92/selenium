'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form" #ссылка

try:
    browser = webdriver.Chrome()
    browser.get(link) #переход по ссылке

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country").send_keys("Russia") #можно так кликать в одной строке
    button = browser.find_elements_by_xpath('//*[@type="submit"]')
    button.click()

finally:
    driver.close()
    time.sleep(30) # успеваем скопировать код за 30 секунд
    browser.quit() # закрываем браузер после всех манипуляций'''

    # не забываем оставить пустую строку в конце файла

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/find_xpath_form'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    inputs = browser.find_elements(By.XPATH, "//*[@class='form-group']/ input")
    for i in inputs:
        i.send_keys('qwerty')
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[ text()='Submit']").click()

    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
    alert.accept()'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    chrome_options = Options()
    driver_service = Service("C:\\chromedriver\\chromedriver.exe")

    starter_link = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome(service=driver_service, options=chrome_options)
        browser.get(starter_link)
        time.sleep(1)

        elements = browser.find_elements(By.CSS_SELECTOR, "input[type=\"text\"]")

        for element in elements:
            element.send_keys("random text")

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type=\"submit\"")
        submit_button.click()

        alert = browser.switch_to.alert
        print("The code from pop-up window is: ", alert.text.split()[-1])
        alert.accept()

    finally:
        browser.close()
        time.sleep(2)
        browser.quit()