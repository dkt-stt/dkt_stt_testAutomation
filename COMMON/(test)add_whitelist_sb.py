from playwright.sync_api import Playwright, sync_playwright, expect
import getpass
import time
import sys

print("")
print("샌드박스 카카오계정 화이트리스트 등록입니다.")
print("LDAP 아이디와 패스워드가 3번 틀릴 경우 프로그램은 종료됩니다.")

# 최대 3번의 로그인 시도
def login(page):
    for i in range(3):
        page.goto("https://sandbox-admin-account.kakao.com/login?return_url=https%3A%2F%2Fsandbox-admin-account.kakao.com%2F")

    # 로그인 절차 - 아이디 입력
        id = input("아이디를 입력해주세요: ")
        page.get_by_placeholder("로그인 아이디").fill(id)

    # 로그인 절차 - 비밀번호 입력
        password = getpass.getpass("패스워드를 입력해주세요: ")
        page.get_by_placeholder("패스워드").fill(password)

        print("")
    # 로그인 절차 - Log in 클릭
        page.get_by_role("button", name="로그인").click()
        page.wait_for_timeout(1000)
        if page.get_by_text("Welcome").is_visible():
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
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 로그인 시도
        if not login(page):
            sys.exit()

        # 화이트리스트 관리 메뉴 이동 
        page.get_by_role("link", name="Tools").click()
        page.get_by_role("link", name="통합 화이트리스트 관리").click()
        # 반복 작업
        while True:
            page.get_by_role("link", name="신규 등록").click()
            # 전화번호 입력
            email = input("화이트 리스트 등록할 아이디 혹은 전화번호를 입력해주세요 : ")
            # 전화번호 입력창에 입력
            page.get_by_placeholder("이메일 또는 전화번호").fill(email)
            # 잘못된 이메일 혹은 전화번호 입력 시 
            try:
                page.get_by_text("입력한 카카오 계정을 등록할 수 없습니다. 테스트계정이 맞는지 확인해주세요")
            except Exception:
                print("입력한 카카오 계정을 등록할 수 없습니다. 테스트계정이 맞는지 확인해주세요.")
                retry = input("계정을 다시 입력하시겠습니까? (Y/N 입력): ").strip().upper()
                print("")
                # Y 외에 입력 경우
                if retry != "Y":
                    print("")
                    print("5초 후에 프로그램이 자동으로 종료됩니다.")
                    time.sleep(5)
                    sys.exit()
            # 정상적으로 입력한 경우
            else:
                # 모든 타겟 체크
                page.locator("#bypass_targets_all").check()
                # 사유 입력
                page.get_by_placeholder("등록 사유를 입력해 주세요 (CRMS 등)").fill("테스트용")
                # 날짜 입력 
                date = input("만료 날짜를 입력해주세요 ex: YYYY-MM-DD : ")
                page.get_by_label("만료일").fill(date)
                # 등록 버튼 선택 
                page.get_by_role("button", name="등록").click()
                # 등록 확인 및 종료 동작 
                print( email + " 화이트리스트 추가 완료")
                # 추가 등록 요청
                retry = input("추가 계정 등록이 필요하십니까? (Y/N 입력): ").strip().upper()
                # Y 외에 입력 경우
                if retry != "Y":
                    print("")
                    print("5초 후에 프로그램이 자동으로 종료됩니다.")
                    browser.close()
                    time.sleep(5)
                    sys.exit()
if __name__ == "__main__":
    main()
