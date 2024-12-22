import pyautogui
import time
import threading
import tkinter as tk
from tkinter import ttk

def start_autoclicker():
    global running
    running = True
    log_label.config(text="오토클리커 실행 중...", foreground="blue")

    click_interval = float(interval_entry.get())
    click_duration = int(duration_entry.get())
    mouse_button = button_var.get()

    def autoclick():
        start_time = time.time()
        try:
            while running:
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time >= click_duration:
                    log_label.config(text="지정된 시간이 종료되었습니다.", foreground="red")
                    break

                pyautogui.click(button=mouse_button)
                time.sleep(click_interval)
        except KeyboardInterrupt:
            log_label.config(text="오토클리커가 중지되었습니다.", foreground="red")

    threading.Thread(target=autoclick).start()

def stop_autoclicker():
    global running
    running = False
    log_label.config(text="오토클리커가 사용자에 의해 중지되었습니다.", foreground="red")

def on_key_press(event):
    if event.keysym == start_key_var.get():
        start_autoclicker()
    elif event.keysym == stop_key_var.get():
        stop_autoclicker()

# GUI 설정
root = tk.Tk()
root.title("오토클리커")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# 클릭 간격
interval_label = ttk.Label(frame, text="클릭 간격 (초):")
interval_label.grid(row=0, column=0, sticky=tk.W)
interval_entry = ttk.Entry(frame, width=10)
interval_entry.grid(row=0, column=1)
interval_entry.insert(0, "0.1")

# 클릭 지속 시간
duration_label = ttk.Label(frame, text="클릭 지속 시간 (초):")
duration_label.grid(row=1, column=0, sticky=tk.W)
duration_entry = ttk.Entry(frame, width=10)
duration_entry.grid(row=1, column=1)
duration_entry.insert(0, "10")

# 마우스 버튼 선택
button_label = ttk.Label(frame, text="마우스 버튼:")
button_label.grid(row=2, column=0, sticky=tk.W)
button_var = tk.StringVar(value="left")
left_button = ttk.Radiobutton(frame, text="왼쪽", variable=button_var, value="left")
left_button.grid(row=2, column=1, sticky=tk.W)
right_button = ttk.Radiobutton(frame, text="오른쪽", variable=button_var, value="right")
right_button.grid(row=2, column=2, sticky=tk.W)

# 시작 키 설정
start_key_label = ttk.Label(frame, text="시작 키:")
start_key_label.grid(row=3, column=0, sticky=tk.W)
start_key_var = tk.StringVar(value="F1")
start_key_dropdown = ttk.Combobox(frame, textvariable=start_key_var, values=[f"F{i}" for i in range(1, 13)], state="readonly")
start_key_dropdown.grid(row=3, column=1)
start_key_dropdown.set("F1")

# 중지 키 설정
stop_key_label = ttk.Label(frame, text="중지 키:")
stop_key_label.grid(row=4, column=0, sticky=tk.W)
stop_key_var = tk.StringVar(value="F2")
stop_key_dropdown = ttk.Combobox(frame, textvariable=stop_key_var, values=[f"F{i}" for i in range(1, 13)], state="readonly")
stop_key_dropdown.grid(row=4, column=1)
stop_key_dropdown.set("F2")

# 로그 출력
log_label = ttk.Label(frame, text="오토클리커 준비 완료.", foreground="blue")
log_label.grid(row=5, column=0, columnspan=3, sticky=tk.W)

# 이벤트 바인딩
root.bind("<KeyPress>", on_key_press)

root.mainloop()
