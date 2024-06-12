from playwright.sync_api import sync_playwright

if True: # Exid 계정정보
    id = "본인 ldap id"
    pw = "본인 ldap pw"
uid = "추가하고 싶은 계정의 uid"
addnum = "추가하고 싶은 횟수"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless 모드를 끄려면 False로 설정
    context = browser.new_context()
    page = context.new_page()

    # exid 이동
    page.goto("https://sandbox-charlie.kakaopage.com/exid/login/?referer=/exid/")
    # 계정정보 입력 후 로그인
    page.get_by_placeholder("LDAP ID 를 입력하세요").fill(id)
    page.get_by_placeholder("패스워드를 입력하세요").fill(pw)
    page.get_by_role("button", name="로그인").click()
    # 고객 조회 이동 후 uid 입력
    page.get_by_text("고객 센터").click()
    page.get_by_text("고객 조회", exact=True).click()
    page.get_by_label("카카오페이지 UID:").fill(uid)
    # 새창 띄우기
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="등록 기기 관리").click()
    page.wait_for_timeout(1000)
    # addnum 횟수만큼 반복 
    for i in range (addnum):
        page1 = page1_info.value
        page1.get_by_role("button", name="횟수부여").click()
        page1.get_by_role("button", name="부여", exact=True).click()
    print(str(addnum) + "회 추가 완료")

    # 브라우저 종료
    context.close()
    browser.close()
