import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
# 1. Navigation 네비게이션 관련 툴
# get, back, forward, refresh

# 1-1. get() 원하는 페이지로 이동하는 함수
# driver.get("https://www.naver.com")
# time.sleep(1)
# driver.get("https://google.com")

# 1-2. back() - 뒤로가기
# driver.back()
# time.sleep(2)

# 1-3. forward() - 앞으로 가기
# driver.forward()
# time.sleep(2)

# 1-4. refresh() - 페이지 새로고침
# driver.refresh()
# time.sleep(2)
# print("동자 끝 ㅅㄱ")

# 2. Browser information
# 2-1. title: 윕 사이트의 타이틀 가지고옴
# driver.get("https://www.naver.com")
# time.sleep(1)

# title = driver.title
# print("title:", title)

# 2-2 current_url 주소창을 그대로 가지고옴
# current_url = driver.current_url
# print("current_url:", current_url)

# if "nid.naver.com" in current_url:
#     print("지금은 로그인하는 로직이 필요함")
# else:
#     print("내가 계획한 로직 그대로 실행하면됨")

# 3. Driver Wait
# 3-1. 3초때 로딩이 끝나서, element가 찾아짐
driver.get("https://www.naver.com")
try:
    selector = "#account > div > a"
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selector)
    )).click()
    print('엘리먼트 로딩 끝')
except Exception as e:
    print(e)
    print("예외 발생, 예외 처리 코드 실행하기")

print("다음 코드 실행")
input()