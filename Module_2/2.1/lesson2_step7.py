from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    select_checkbox = browser.find_element_by_id("robotCheckbox")
    select_checkbox.click()
    select_checkbox = browser.find_element_by_id("robotsRule")
    select_checkbox.click()
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
