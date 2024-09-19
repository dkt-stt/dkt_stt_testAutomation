# other_code.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def execute_code(user_id, user_pw, uid, add):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Headless 모드 추가

    # Selenium 웹 드라이버 설정
    driver = webdriver.Chrome(options=chrome_options)

    # 암묵적 대기 설정 (페이지 로딩 기다림)
    driver.implicitly_wait(10)

    # exid 이동
    driver.get("https://sandbox-charlie.kakaopage.com/exid/login/?referer=/exid/")

    # 계정정보 입력 후 로그인
    driver.find_element(By.CSS_SELECTOR, '#user_id').send_keys(user_id)
    driver.find_element(By.CSS_SELECTOR, '#user_pw').send_keys(user_pw)
    driver.find_element(By.CSS_SELECTOR, '#loginForm > div:nth-child(5) > div > button').click()

    # 고객 센터 이동 후 uid 입력
    driver.get("https://sandbox-charlie.kakaopage.com/exid/customer/user/lookup/v2/")
    driver.find_element(By.CSS_SELECTOR, '#id_kakaopage_uid').send_keys(uid)

    # 새 창 띄우기
    main_window = driver.current_window_handle  # 메인 윈도우 핸들 저장
    driver.find_element(By.CSS_SELECTOR, '#wrapper > div > div:nth-child(8) > button').click()

    # 새로 열린 창으로 전환
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # 새로운 창이 열릴 때까지 대기
    new_window = [window for window in driver.window_handles if window != main_window][0]
    driver.switch_to.window(new_window)

    # add 횟수만큼 반복
    for i in range(add):
        driver.find_element(By.CSS_SELECTOR, '#wrapper > div > div:nth-child(4) > div.col-md-8.right > button').click()
        driver.find_element(By.CSS_SELECTOR, '#add-bonus-btn').click()

    print(str(add) + "회 추가 완료")

    # 브라우저 종료
    driver.quit()
