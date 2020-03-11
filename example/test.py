from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://google.co.kr"

driver = webdriver.Chrome('../driver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get(url)

time.sleep(5)
driver.quit()