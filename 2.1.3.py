import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = " http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

print(x)
print(y)

option = browser.find_element(By.ID, "answer").send_keys(calc(x))
option1 = browser.find_element(By.ID, "robotCheckbox").click()
option2 = browser.find_element(By.ID, "robotsRule").click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
time.sleep(10)
browser.quit()
