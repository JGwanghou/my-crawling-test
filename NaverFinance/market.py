import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 가상머신 접속
# 1. python -m venv myenv
# 2. .\myenv\Scripts\activate
# 보안 오류 발생할 수 있음. -> 관리자 권한으로 실행해서 명령어 2개 쳐야함 검색ㄱ
# pip install selenium, pandas, lxml

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="
driver = webdriver.Chrome()
driver.get(url)

checkboxes = driver.find_elements(By.NAME, 'fieldIds')
items_to_select = ['영업이익', '부채총계', '주당순이익']

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
    parent = checkbox.find_element(By.XPATH, '..') # 부모
    label = parent.find_element(By.TAG_NAME, 'label')
    # print(label.text)

    if label.text in items_to_select:
        checkbox.click()
    
# 적용하기 클릭
btn_apply = driver.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 40):
    driver.get(url + str(idx))
    
    df = pd.read_html(driver.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:
        break

    # 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): # 파일이 있으면 헤더 (종목명, 현재가 등) 제외
        df.to_csv(f_name, encoding="utf-8-sig", index=False, mode='a', header=False)
    else: # 파일이 없다면
        df.to_csv(f_name, encoding="utf-8-sig", index=False)

    print(f'{idx} 페이지가 완료되었습니다.')

driver.quit()