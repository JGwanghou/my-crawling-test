# pip install selenium, webdriver_manager
import openpyxl

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# DriverManager가 알아서 크롬 드라이버 설치
service = Service(executable_path=ChromeDriverManager().install())
drvier = webdriver.Chrome(service=service)

drvier.get("https://www.naver.com/")