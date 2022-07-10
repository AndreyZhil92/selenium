from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')

    for element in elements:
        element.send_keys('Z')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()


'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/huge_form.html'
with webdriver.Chrome() as browser:
    browser.get(url=url)
    [i.send_keys('werty') for i in browser.find_elements(By.CSS_SELECTOR, '.first_block input')]
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(30)'''

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("Курва")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(15)
    '''

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.XPATH, '//*[@type="text"]')
    for element in elements:
        element.send_keys("test")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла'''



