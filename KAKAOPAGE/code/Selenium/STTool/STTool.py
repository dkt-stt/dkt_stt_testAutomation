# 모듈 불러오기
import os
import sys 
import tkinter as tk
import tkinter.font
import tkinter.messagebox as msgbox
import webbrowser
from PIL import Image, ImageTk
from tkinter import ttk
from exid_add import execute_code  # other_code.py에서 함수 가져오기

# 전역 변수 선언 (각 프레임마다 구별되므로 전역 변수를 선언해야 함)
id_entry = None
pw_entry = None
uid_entry = None
add_entry = None
img = None

# 작업 완료 시 메시지 박스를 출력하는 함수
def show_completion_message():
    msgbox.showinfo("완료", "작업이 완료되었습니다.")

# 기기제한 늘리기 버튼 클릭 시 동작
def on_button_click():
    user_id = id_entry.get()  # 입력된 ID 값 가져오기
    user_pw = pw_entry.get()  # 입력된 PW 값 가져오기
    uid = uid_entry.get()  # 입력된 uid 값 가져오기
    add = add_entry.get()  # 입력된 추가횟수 값 가져오기

    # 필드 미입력 시 오류 메시지 박스 노출 (추가 횟수 1 ~ 20 사이의 정수가 아닐 경우 오류 팝업 노출)
    if not user_id or not user_pw or not uid or not add.isdigit() or not (1 <= int(add) <= 20):
        msgbox.showwarning("입력 오류", "모든 필드를 올바르게 입력하세요.")
        return
    
    # 입력받은 계정정보를 other_code로 보내줌
    result = execute_code(user_id, user_pw, uid, int(add))

    if result:  # result가 True일 경우에만 메시지 박스 출력
        show_completion_message()

# 크레딧 팝업 버튼
def credit_button_click():
    msgbox.showinfo("알림", "DKTechin \n 스토리테스트기술팀")

# 위키 이동 버튼
def wiki_button_click():
    url = 'https://wiki.daumkakao.com/pages/viewpage.action?pageId=1337159497'
    webbrowser.open(url)

# 깃허브 이동 버튼
def git_button_click():
    url = 'https://github.com/dkt-stt/dkt_stt_testAutomation'
    webbrowser.open(url)

# Tkinter 창, 테마, 폰트, 해상도 설정
window = tk.Tk()
s = ttk.Style()
s.theme_use('alt')
window.tk.call('tk', 'scaling', 3.0)
window.geometry("470x700")
window.title("스토리테스트기술팀 자동화 툴")
font=tkinter.font.Font(family="맑은 고딕", size=15)

# 창 크기 고정하기 (t/f)
window.resizable(False, False)

# Notebook 생성 (탭 생성)
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill='both')

# tab1 프레임 구성요소 설정
def create_tab1_content(frame):
    global img, id_entry, pw_entry, uid_entry, add_entry

# 이미지 첨부 파일의 절대경로 설정 
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    img_path = os.path.join(base_path, 'cover.png')

    # 이미지 불러오기 및 크기 조정
    img = Image.open(img_path)
    img = img.resize((400, 300)) 
    img = ImageTk.PhotoImage(img)

    # 이미지 삽입
    label = tk.Label(frame, image=img)
    label.pack()

    # 계정정보 입력을 위한 프레임 생성
    input_frame = tk.Frame(frame)
    input_frame.pack(pady=10)

    # ID 입력 레이블과 입력창
    id_label = tk.Label(input_frame, text="LDAP ID :", font = font)
    id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    id_entry = tk.Entry(input_frame)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    # PW 입력 레이블과 입력창
    pw_label = tk.Label(input_frame, text="LDAP PW :", font = font)
    pw_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    pw_entry = tk.Entry(input_frame, show="*")  # 비밀번호는 *로 표시
    pw_entry.grid(row=1, column=1, padx=5, pady=5)

    # UID 입력 레이블과 입력창
    uid_label = tk.Label(input_frame, text="추가할 계정의 UID :", font = font)
    uid_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    uid_entry = tk.Entry(input_frame)
    uid_entry.grid(row=2, column=1, padx=5, pady=5)

    # 기기 제한 횟수 입력 레이블과 입력창
    add_label = tk.Label(input_frame, text="추가 횟수 :", font = font)
    add_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    add_entry = tk.Entry(input_frame)
    add_entry.grid(row=3, column=1, padx=5, pady=5)
    add_label_info = tk.Label(input_frame, text="* 1 ~ 20 정수만 입력 가능 ", font = ("맑은고딕",10), fg = "grey")
    add_label_info.grid(row=4, column=1, padx=1, pady=1)

    # 늘리기 버튼 생성
    start_button = tk.Button(frame, text="기기제한 늘리기", font = font, command=on_button_click)
    start_button.pack(pady=3)

    # 종료 버튼 생성
    exit_button = tk.Button(frame, text="종료",font = font, command=window.quit)
    exit_button.pack(pady=3)

    # Credit 버튼 생성
    credit_button = tk.Button(frame, text="만든 사람", font = ("맑은고딕",12), command=credit_button_click)
    credit_button.pack(side="right", anchor="s")

    # 안내 문구 생성
    info_label = tk.Label(frame, text="※ 샌드박스 환경 사내망 연결 필수\n 카카오페이지 계정 기기제한 등록 횟수 늘리기", font = ("맑은고딕",13), fg = "grey")
    info_label.pack(side="left", anchor= "s")

# tab2 프레임 구성요소 설정
def create_tab2_content(frame):
    label = tk.Label(frame, text="커밍 순", font=("맑은 고딕", 20))
    label.pack(pady=20)

# tab3 프레임 구성요소 설정
def create_tab3_content(frame):
    label = tk.Label(frame, text="커밍 순", font=("맑은 고딕", 30))
    label.pack(pady=20)

# tab4 프레임 구성요소 설정
def create_tab4_content(frame):
    label = tk.Label(frame, text="커밍 순", font=("맑은 고딕", 40))
    label.pack(pady=20)

# tab5 프레임 구성요소 설정
def create_tab5_content(frame):
    wiki_button = tk.Button(frame, text="스토리테스트기술팀 위키", font = ("맑은고딕",15), command=wiki_button_click)
    wiki_button.pack(side="top")
    
    git_button = tk.Button(frame, text="스토리테스트기술팀 깃허브" , font = ("맑은고딕",15), command=git_button_click)
    git_button.pack(side="top")

# 탭1 생성
tab1 = tk.Frame(notebook)
create_tab1_content(tab1) 
notebook.add(tab1, text="EXID 기기제한 늘리기")

# 탭2 생성
tab2 = tk.Frame(notebook)
create_tab2_content(tab2) 
notebook.add(tab2, text="추가 1")

# 탭3 생성
tab3 = tk.Frame(notebook)
create_tab3_content(tab3) 
notebook.add(tab3, text="추가 2")

# 탭4 생성
tab4 = tk.Frame(notebook)
create_tab4_content(tab4) 
notebook.add(tab4, text="추가 3")

# 탭5 생성
tab5 = tk.Frame(notebook)
create_tab5_content(tab5) 
notebook.add(tab5, text="유용한 링크")

# Tkinter 실행유지
window.mainloop()
