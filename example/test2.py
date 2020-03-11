from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../driver/chromedriver.exe")
driver.implicitly_wait(3)

driver.fullscreen_window()
# driver.set_window_rect(100, 100, 100, 100)

time.sleep(3)
driver.close()
