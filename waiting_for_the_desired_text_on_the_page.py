from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # wait whene price will be 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))

    # after click button book
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    answer = calc(x)

    input_result = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_result.send_keys(answer)
    
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
    
finally:
    time.sleep(10)
    browser.quit()