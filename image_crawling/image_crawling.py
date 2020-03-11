from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from tqdm import tqdm

keyword = input("수집할 이미지 : ")
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword)
driver = webdriver.Chrome('../driver/chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

# 웹 페이지 가져오기
driver.get(url)

# 스크롤 다운
body = driver.find_element_by_css_selector('body')

for i in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# 이미지 요소(elements) 수집하기
imgs = driver.find_elements_by_css_selector('img._img')
print(len(imgs))

links = []

for img in imgs:
    link = img.get_attribute('src')
    if 'http' in link:
        links.append(link)
## 폴더 생성
import os
if not os.path.isdir('./{}'.format(keyword)):
    os.mkdir('./{}'.format(keyword))
print('[폴더생성]')

## 다운로드 - 파일이름(확장자)
for index, link in tqdm(enumerate(links), total=len(links)):
    start = link.rfind('.')
    end = link.rfind('&')

    filetype = link[start:end]
    if '%' in filetype:
        end = filetype.find('%')
        filetype = filetype[:end]

    filename = "./{0}/{0}{1:3d}{2}".format(keyword, index, filetype)
    urlretrieve(link, filename)
print('[다운로드 완료]')

## 압축
import zipfile
zip_file = zipfile.ZipFile('./{}.zip'.format(keyword), 'w')
for image in os.listdir('./{}'.format(keyword)):
    zip_file.write('./{}/{}'.format(keyword, image))

zip_file.close()
print("[압축완료]")

time.sleep(3)
driver.quit()