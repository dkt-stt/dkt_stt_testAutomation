# other_code
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def execute_code(user_id, user_pw, uid, add):    
    # 크롬 옵션 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # 필요시 주석 처리
    chrome_options.add_argument("--window-size=1920,1080")  # 브라우저 창 크기 설정

    # Selenium 웹 드라이버 설정
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # exid 페이지로 이동
        driver.get("https://sandbox-charlie.kakaopage.com/exid/login/?referer=/exid/")

        # 계정 정보 입력 후 로그인 (명시적 대기 사용)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#user_id'))).send_keys(user_id)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#user_pw'))).send_keys(user_pw)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginForm > div:nth-child(5) > div > button'))).click()

        # 계정 로그인 유효성 체크 
        try:
            if driver.find_element(By.XPATH, "//*[text()='Sign Out']"):
                print(f"안녕하세요 {user_id}, {uid} 계정의 기기 등록 횟수 {add}회 추가합니다.")
        except NoSuchElementException:
            print("아이디 또는 비밀번호가 잘못되었습니다.")
            return False # 실패

        # 고객 센터 페이지로 이동 후 uid 입력
        driver.get("https://sandbox-charlie.kakaopage.com/exid/customer/user/lookup/v2/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id_kakaopage_uid'))).send_keys(uid)

        # 새 창 띄우기
        main_window = driver.current_window_handle  # 메인 윈도우 핸들 저장
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wrapper > div > div:nth-child(8) > button'))).click()

        # 새로 열린 창으로 전환
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # 새 창이 열릴 때까지 대기
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)

        # add 횟수만큼 반복
        for i in range(add):
            try:
                # 버튼이 표시되고 클릭할 수 있는 상태인지 확인 후 클릭
                button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#wrapper > div > div:nth-child(4) > div.col-md-8.right > button')))

                if button.is_displayed():  # 버튼이 표시되었는지 확인
                    button.click()
                else:
                    print("버튼이 화면에 표시되지 않음")

                # 보너스 추가 버튼 클릭
                add_bonus_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#add-bonus-btn')))
                add_bonus_button.click()

            except NoSuchElementException as e:
                print(f"클릭 에러 발생: {e}")
                continue

        print(str(add) + "회 추가 완료")
        return True # 작업 성공

    except TimeoutException as e:
        print(f"타임아웃 발생: {e}")
        return False # 작업 실패 
    
    except NoSuchElementException as e:
        print(f"엘리먼트를 찾을 수 없습니다: {e}")
        return False # 작업 실패 
    
    finally:
        # 브라우저 종료
        driver.quit()