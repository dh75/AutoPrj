from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../driver/chromedriver.exe")
driver.implicitly_wait(3)

driver.get("http://www.naver.com")
driver.get("https://google.co.kr")
driver.get("http://www.youtube.com")

driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)

time.sleep(3)
driver.close()
