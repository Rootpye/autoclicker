import pyautogui
import time
import threading
import tkinter as tk
from tkinter import ttk

def start_autoclicker():
    global running
    running = True

    click_interval = float(interval_entry.get())
    mouse_button = button_var.get()
    click_duration = duration_entry.get()

    def autoclick():
        start_time = time.time()
        try:
            while running:
                if click_duration:
                    current_time = time.time()
                    elapsed_time = current_time - start_time

                    if elapsed_time >= float(click_duration):
                        log_label.config(text="The specified time has ended.", foreground="red")
                        break

                pyautogui.click(button=mouse_button)
                time.sleep(click_interval)
        except KeyboardInterrupt:
            log_label.config(text="The autoclicker has stopped.", foreground="red")

    threading.Thread(target=autoclick).start()

def stop_autoclicker():
    global running
    running = False
    log_label.config(text="The autoclicker was stopped by the user.", foreground="red")

def on_key_press(event):
    if event.keysym == start_key_var.get():
        start_autoclicker()
    elif event.keysym == stop_key_var.get():
        stop_autoclicker()

# GUI Settings
root = tk.Tk()
root.title("Autoclicker")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Click Interval
interval_label = ttk.Label(frame, text="Click Interval (seconds):")
interval_label.grid(row=0, column=0, sticky=tk.W)
interval_entry = ttk.Entry(frame, width=10)
interval_entry.grid(row=0, column=1)
interval_entry.insert(0, "0.1")

# Click Duration
# If left empty, it runs indefinitely
duration_label = ttk.Label(frame, text="Click Duration (seconds, leave blank for infinite):")
duration_label.grid(row=1, column=0, sticky=tk.W)
duration_entry = ttk.Entry(frame, width=10)
duration_entry.grid(row=1, column=1)

# Mouse Button Selection
button_label = ttk.Label(frame, text="Mouse Button:")
button_label.grid(row=2, column=0, sticky=tk.W)
button_var = tk.StringVar(value="left")
left_button = ttk.Radiobutton(frame, text="Left", variable=button_var, value="left")
left_button.grid(row=2, column=1, sticky=tk.W)
right_button = ttk.Radiobutton(frame, text="Right", variable=button_var, value="right")
right_button.grid(row=2, column=2, sticky=tk.W)

# Start Key Setting
start_key_label = ttk.Label(frame, text="Start Key:")
start_key_label.grid(row=3, column=0, sticky=tk.W)
start_key_var = tk.StringVar(value="F1")
start_key_dropdown = ttk.Combobox(frame, textvariable=start_key_var, values=[f"F{i}" for i in range(1, 13)], state="readonly")
start_key_dropdown.grid(row=3, column=1)
start_key_dropdown.set("F1")

# Stop Key Setting
stop_key_label = ttk.Label(frame, text="Stop Key:")
stop_key_label.grid(row=4, column=0, sticky=tk.W)
stop_key_var = tk.StringVar(value="F2")
stop_key_dropdown = ttk.Combobox(frame, textvariable=stop_key_var, values=[f"F{i}" for i in range(1, 13)], state="readonly")
stop_key_dropdown.grid(row=4, column=1)
stop_key_dropdown.set("F2")

# Log Output
log_label = ttk.Label(frame, text="Autoclicker is ready.", foreground="black")
log_label.grid(row=5, column=0, columnspan=3, sticky=tk.W)

# Event Binding
root.bind("<KeyPress>", on_key_press)

root.mainloop()
