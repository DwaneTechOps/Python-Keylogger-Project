import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def record_key(event):
    key = event.keysym

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp}] Key pressed: {key}\n"

    output.insert(tk.END, log_entry)
    output.see(tk.END)

def save_log():
    log_text = output.get("1.0", tk.END)

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(log_text)

window = tk.Tk()
window.title("Keyboard Input Monitor")
window.geometry("500x400")

label = tk.Label(
    window,
    text="Click inside the input box and type"
)
label.pack(pady=10)

input_box = tk.Entry(window, width=50)
input_box.pack(pady=10)
input_box.bind("<KeyPress>", record_key)

output = tk.Text(window, height=12, width=55)
output.pack(pady=10)

save_button = tk.Button(
    window,
    text="Save Log",
    command=save_log
)
save_button.pack(pady=10)

def clear_log():
    output.delete("1.0", tk.END)

clear_button = tk.Button(
    window,
    text="Clear Log",
    command=clear_log
)
clear_button.pack(pady=10)

window.mainloop()