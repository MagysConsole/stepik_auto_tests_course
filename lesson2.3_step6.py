from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    button_click = browser.find_element_by_tag_name('button').click()
    new_window = browser.window_handles
    switch_window = browser.switch_to.window(new_window[1])
    captcha = browser.find_element_by_id('input_value').text

    input_answer = browser.find_element_by_id('answer').send_keys(calc(captcha))
    button_click_1 = browser.find_element_by_class_name('btn.btn-primary').click()

finally:
    secret = browser.switch_to.alert
    secret_txt = secret.text.split(': ')[-1]
    time.sleep(5)
    secret.accept()
    time.sleep(5)
    browser.close()  # Каша с очередность закрытия окна.
    print(secret_txt)
