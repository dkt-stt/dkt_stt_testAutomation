import os
import sys
import tkinter as tk
import tkinter.font
import tkinter.messagebox as msgbox
from other_code import execute_code  # other_code.py에서 함수 가져오기

# 입력정보 받음
def on_button_click():
    user_id = id_entry.get()  # 입력된 ID 값 가져오기
    user_pw = pw_entry.get()  # 입력된 PW 값 가져오기
    uid = uid_entry.get()  # 입력된 uid 값 가져오기
    num = num_entry.get()  # 입력된 추가횟수 값 가져오기
    # 입력 정보 출력 (비번은 제외)
    print(f" 안녕하세요,{user_id}, UID:{uid} 계정의 기기 등록 횟수{num}회 추가합니다.")

    # 입력받은 함수를 보내줌
    execute_code(user_id, user_pw, uid, int(num))
    
    # 실행이 완료된 후 완료 메시지 표시
    msgbox.showinfo("완료", "작업이 완료되었습니다.")

# 크레딧
def credit_button_click():
    msgbox.showinfo("알림", "DKTechin \n 스토리테스트기술팀")

# Tkinter 창, 폰트 설정
window = tk.Tk()
window.geometry("400x700")
window.title("스토리테스트기술팀 자동화 툴")
font=tkinter.font.Font(family="맑은 고딕", size=15)

# 창 크기 고정 
window.resizable(False, False)

# 이미지 첨부 파일의 절대경로 설정 
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

img_path = os.path.join(base_path, 'cover.png')

# 이미지 로드
img = tk.PhotoImage(file=img_path) # 이미지 파일 경로

# 이미지 삽입
label = tk.Label(window, image=img)
label.pack()

# ID와 PW 입력을 위한 프레임 생성
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# ID 입력 레이블과 입력창
id_label = tk.Label(input_frame, text="ID :", font = font)
id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
id_entry = tk.Entry(input_frame)
id_entry.grid(row=0, column=1, padx=5, pady=5)

# PW 입력 레이블과 입력창
pw_label = tk.Label(input_frame, text="PW :", font = font)
pw_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
pw_entry = tk.Entry(input_frame, show="*")  # 비밀번호는 *로 표시
pw_entry.grid(row=1, column=1, padx=5, pady=5)

# UID 입력 레이블과 입력창
uid_label = tk.Label(input_frame, text="추가할 계정의 UID :", font = font)
uid_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
uid_entry = tk.Entry(input_frame)
uid_entry.grid(row=2, column=1, padx=5, pady=5)

# 기기 제한 횟수 입력 레이블과 입력창
num_label = tk.Label(input_frame, text="추가 횟수 :", font = font)
num_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
num_entry = tk.Entry(input_frame)
num_entry.grid(row=3, column=1, padx=5, pady=5)
num_label_add = tk.Label(input_frame, text="* 권장사항 : 1 ~ 20 회  ", font = ("맑은고딕",10), fg = "grey")
num_label_add.grid(row=4, column=1, padx=1, pady=1)

# 적용 버튼 생성
start_button = tk.Button(window, text="기기제한 늘리기", font = font, command=on_button_click)
start_button.pack(pady=3)

# 종료 버튼 생성
exit_button = tk.Button(window, text="종료",font = font, command=window.quit)
exit_button.pack(pady=3)

# Credit 버튼 생성
credit_button = tk.Button(window, text="만든 사람", font = ("맑은고딕",10), command=credit_button_click)
credit_button.pack(side="right")

# Tkinter 루프 실행
window.mainloop()
