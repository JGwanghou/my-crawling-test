# pip install selenium, webdriver_manager

# 크롬 드라이버 기본 모듈
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 자동 업데이트을 위한 모듈
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

#-------------- 기본 설정 --------------------- #

# 웹페이지 해당 주소 이동
browser.get("https://shopping.naver.com/home")

# 쇼핑창 화면에서 검색input 클릭하고 검색실행
search = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
search.click()
browser.implicitly_wait(3)

search.send_keys('아이폰')
search.send_keys(Keys.ENTER)

before_h = browser.execute_script("return window.scrollY")
while True:
    body = browser.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)
    time.sleep(1)

    after_h = browser.execute_script("return window.scrollY")

    if before_h == after_h:
        break
    before_h = after_h

titles = browser.find_element(By.CLASS_NAME, 'product_link__TrAac')
for title in titles:
    print(title)    


# 엑셀 생성
# wb = openpyxl.Workbook()
# ws = wb.create_sheet('테스트 시트')

# 데이터 추가
# ws['A1'] = '참가번호'
# ws['B1'] = '성명'
# 
# ws['A2'] = '1'
# ws['B2'] = '김댕댕'

# wb.save('sample.xlsx')

