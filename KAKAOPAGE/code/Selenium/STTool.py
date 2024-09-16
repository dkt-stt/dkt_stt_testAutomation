import tkinter as tk
from other_code import execute_code  # other_code.py에서 함수 가져오기


# 입력정보 받음
def on_button_click():
    user_id = id_entry.get()  # 입력된 ID 값 가져오기
    user_pw = pw_entry.get()  # 입력된 PW 값 가져오기
    uid = uid_entry.get()  # 입력된 uid 값 가져오기
    num = uid_entry.get()  # 입력된 추가횟수 값 가져오기
    print(f"ID: {user_id}, PW: {user_pw}, UID: {uid}, 추가 횟수: {num}")

    # 여기서 execute_code 함수에 필요한 값을 넘겨줄 수 있습니다.
    execute_code(user_id, user_pw, uid, int(num))

# Tkinter 창 설정
window = tk.Tk()
window.geometry("400x700")
window.title("스토리테스트기술팀 자동화 툴")

# 창 크기 고정 (크기 조절 불가)
# window.resizable(False, False)

# PhotoImage를 사용하여 이미지 로드 (PNG 또는 GIF)
img = tk.PhotoImage(file="/Users/andy.sc/Desktop/dkt_stt_testAutomation/KAKAOPAGE/code/Selenium/cover.png")  # 이미지 파일 경로

# Label 위젯에 이미지 삽입
label = tk.Label(window, image=img)
label.pack()

# ID와 PW 입력을 위한 프레임 생성
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# ID 입력을 위한 레이블과 입력창을 한 줄에 배치
id_label = tk.Label(input_frame, text="ID :")
id_label.grid(row=0, column=0, padx=5, pady=5)
id_entry = tk.Entry(input_frame)
id_entry.grid(row=0, column=1, padx=5, pady=5)

# PW 입력을 위한 레이블과 입력창을 한 줄에 배치
pw_label = tk.Label(input_frame, text="PW :")
pw_label.grid(row=1, column=0, padx=5, pady=5)
pw_entry = tk.Entry(input_frame, show="*")  # 비밀번호는 *로 표시
pw_entry.grid(row=1, column=1, padx=5, pady=5)

# UID 입력을 위한 레이블과 입력창을 한 줄에 배치
uid_label = tk.Label(input_frame, text="추가할 계정의 UID :")
uid_label.grid(row=2, column=0, padx=5, pady=5)
uid_entry = tk.Entry(input_frame)
uid_entry.grid(row=2, column=1, padx=5, pady=5)

# 기기 제한 횟수 입력을 위한 레이블과 입력창
num_label = tk.Label(input_frame, text="추가 횟수 :")
num_label.grid(row=3, column=0, padx=5, pady=5)
num_entry = tk.Entry(input_frame)
num_entry.grid(row=3, column=1, padx=5, pady=5)

# 적용 버튼 생성
start_button = tk.Button(window, text="기기제한 늘리기", command=on_button_click)
start_button.pack(pady=3)

# 종료 버튼 생성
exit_button = tk.Button(window, text="종료", command=window.quit)
exit_button.pack(pady=3)

# Tkinter 루프 실행
window.mainloop()
