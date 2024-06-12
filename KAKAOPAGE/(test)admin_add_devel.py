import getpass
import time
import sys
from playwright.sync_api import sync_playwright


print("")
print("안녕하세요. Kakaopage 기기 등록 제한 추가 요청입니다.")
print("LDAP 아이디와 패스워드가 3번 틀릴 경우 프로그램은 종료됩니다.")
print("sdfsdf")

# 최대 3번의 로그인 시도
def login(page):
    for i in range(3):
        page.goto("https://sandbox-charlie.kakaopage.com/exid/login/?referer=/exid/")

    # 로그인 절차 - 아이디 입력
        id = input("아이디를 입력해주세요: ")
        page.get_by_placeholder("LDAP ID 를 입력하세요").fill(id)

    # 로그인 절차 - 비밀번호 입력
        password = getpass.getpass("패스워드를 입력해주세요: ")
        page.get_by_placeholder("패스워드를 입력하세요").fill(password)

        print("")
    # 로그인 절차 - Log in 클릭
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(1000)
        if page.get_by_text("Sign Out").is_visible():
            # 로그인 성공 시 LDAP 확인
            LDAP = id
            print("안녕하세요 " + LDAP + " !")
            # for문 탈출
            return True
        else:
            print("아이디 또는 비밀번호가 잘못되었습니다.")
            print("")
            if i == 2:
                print("최대 시도 횟수를 초과하였습니다.")
                print("5초 후에 프로그램이 자동으로 종료됩니다.")
                time.sleep(5)
                return False
    return False
def main():
    with sync_playwright() as p:
        # 브라우저 생성
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # 로그인 시도
        if not login(page):
            sys.exit()
        # 반복 작업
        while True:
            # 고객 센터 > 고객 조회 이동
            page.get_by_text("고객 센터").click()
            page.get_by_text("고객 조회", exact=True).click()
            uid = input("추가하려는 계정의 UID를 입력해주세요: ")
            page.get_by_label("카카오페이지 UID:").fill(uid)

            # 1초 대기
            time.sleep(1)

            # 새창 띄우고 동록기기 관리 화면으로 이동
            with page.expect_popup() as page1_info:
                page.get_by_role("button", name="등록 기기 관리").click()

            # addnum 횟수만큼 반복 
            addnum = input("추가하려는 횟수를 입력해주세요: ")
            for i in range (int(addnum)):
                page1 = page1_info.value
                page1.get_by_role("button", name="횟수부여").click()
                page1.get_by_role("button", name="부여", exact=True).click()
            print(str(addnum) + "회 추가 완료")

            print("5초 후에 프로그램이 자동으로 종료됩니다.")
            browser.close()
            time.sleep(5)
            sys.exit()
if __name__ == "__main__":
    main()

