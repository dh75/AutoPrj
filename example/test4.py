from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("../driver/chromedriver.exe")
driver.implicitly_wait(3)

# 페이지 이동
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%8A%B4%EB%8F%84%EC%B9%98")

# 검색창을 찾고 변수에 저장
search = driver.find_element_by_css_selector()

time.sleep(3)
driver.close()
