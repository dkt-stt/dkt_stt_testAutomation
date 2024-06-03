import getpass
import time
import sys
from playwright.sync_api import sync_playwright

print("")
print("안녕하세요. KakaoTalk Sandbox Admin 인증번호 요청입니다.")
print("아이디와 패스워드가 3번 틀릴 경우 프로그램은 종료됩니다.")
print("")

# 최대 3번의 로그인 시도
def login(page):
    for i in range(3):
        page.goto("https://sandbox-admin.talk.kakao.com/")

    # 로그인 절차 - 아이디 입력
        id = input("아이디를 입력해주세요: ")
        page.get_by_placeholder("아이디").fill(id)

    # 로그인 절차 - 비밀번호 입력
        password = getpass.getpass("패스워드를 입력해주세요: ")
        page.get_by_placeholder("비밀번호").fill(password)

        print("")
    # 로그인 절차 - Log in 클릭
        page.get_by_role("button", name="Log in").click()
        if page.title() == "Kakaotalk Admin":
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
            # 사내 번호 관리 진입
            page.click("text=SMS 발송내역 조회")

            # 전화번호 입력
            phonenumber = input('인증번호를 요청한 전화번호를 입력해 주세요 : ')

            # 전화번호 입력창에 입력
            page.fill('input[name="phone_number"]', phonenumber)

            # 체크 클릭
            page.click('input[name="commit"]')

            # 1초 쉼
            time.sleep(1)

            # 해당 문구가 노출된 경우(번호 잘못 입력한 경우)
            try:
                element = page.text_content('//*[@id="sms-pane-search"]/table[2]/tbody/tr[1]/td[5]')
            except Exception:
                print("")
                print("인증번호가 존재하지 않습니다.")
                retry = input("번호를 다시 입력하시겠습니까? (Y/N 입력): ").strip().upper()
                print("")
                # Y 외에 입력 경우
                if retry != "Y":
                    print("")
                    print("5초 후에 프로그램이 자동으로 종료됩니다.")
                    time.sleep(5)
                    sys.exit()
            # 정상적으로 입력한 경우
            else:
                print("")
                # 요청한 번호의 인증코드
                PhoneCode = page.text_content('//*[@id="sms-pane-search"]/table[2]/tbody/tr[1]/td[5]')
                print("인증번호 :" + PhoneCode)

                # 인증코드 요청시간
                PhoneCode_time = page.text_content('//*[@id="sms-pane-search"]/table[2]/tbody/tr[1]/td[6]')
                print("요청시간 :" + PhoneCode_time)
                print("")

                retry = input("추가 인증코드가 필요하십니까? (Y/N 입력): ").strip().upper()
                # Y 외에 입력 경우
                if retry != "Y":
                    print("")
                    print("5초 후에 프로그램이 자동으로 종료됩니다.")
                    browser.close()
                    time.sleep(5)
                    sys.exit()
if __name__ == "__main__":
    main()