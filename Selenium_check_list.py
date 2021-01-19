import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with open("test.txt", "w") as file:             # открыть фойл или зоздать новый
    content = file.write("automationbypython")  # create test.txt file

# открыть сайт в браузере
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

# Найти элемент по css селектору и ввести значение в поле
input1 = browser.find_element_by_name('firstname')      # найти элемент по css селектору
input1.send_keys('Ivan')                                # и ввести значение

# Открыть список и выбрать элемент
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"

# Проскролить страницу на 100 пикселей
browser.execute_script("window.scrollBy(0, 100);")
# Проскролит страницу до нужного элемента
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# Загрузка файла
current_dir = os.path.abspath(os.path.dirname('')) # указать директорию и вставить файл
file_path = os.path.join(current_dir, "test.txt")
element = browser.find_element(By.ID, 'file')
element.send_keys(file_path)

option1 = browser.find_element_by_id("robotCheckbox")   # найти и нажать флажок или кнопку
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_css_selector("button.btn")  # найти кнопку и нажать
button.click()

# Всплывающие окна
answer = browser.switch_to.alert  # вывести на экран последний элемент всплывающего окна
answer_text = answer.text
answer.accept()
print(answer_text.split()[-1])

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

# Выбор открытых ссылок
new_window = browser.window_handles[1]  # имя второй открытой ссылки и переход на неё
browser.switch_to.window(new_window)
first_window = browser.window_handles[0]

# Неявное ожидание
browser.implicitly_wait(5)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )



time.sleep(10)
# Закрытие браузера
browser.quit()
