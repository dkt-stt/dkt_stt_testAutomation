import re
import random
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless 모드를 끄려면 False로 설정
    context = browser.new_context()
    page = context.new_page()
    # 원하는 작업 수행
    # 예: 요소 클릭, 텍스트 입력 등
    
    page.goto("https://www.google.com/")
    for i in range(10):
        text_list = ['사과', '딸기', '포도', '자몽', '망고', '바나나']
        random_text = random.choice(text_list)
        page.get_by_label("검색", exact=True).fill(random_text)
        page.wait_for_timeout(500)
        page.keyboard.press("Enter")
        page.wait_for_timeout(500)
        page.go_back()
        page.reload()

    # 브라우저 종료
    context.close()
    browser.close()
