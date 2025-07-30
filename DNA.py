# Builder Alireza Amjadi 
# https://github.com/alirezaamjadi

import os
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox

def save_note(name, title, content):
    base_folder = "DNA KHATERAT"
    if not os.path.exists(base_folder):
        os.mkdir(base_folder)

    today = datetime.now().strftime("%Y_%m_%d")
    folder_name = os.path.join(base_folder, today)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    existing_notes = [f for f in os.listdir(folder_name) if f.startswith("note") and f.endswith(".txt")]
    note_number = len(existing_notes) + 1
    filename = os.path.join(folder_name, f"note{note_number}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"تاریخ: {datetime.now().strftime('%Y/%m/%d')}\n")
        f.write(f"نام: {name}\n")
        f.write(f"عنوان: {title.upper()}\n\n")
        f.write(content)
    messagebox.showinfo("موفقیت", f"یادداشت شما ذخیره شد در فایل {filename}")

def main():
    root = tk.Tk()
    root.withdraw()

    name = simpledialog.askstring("نام کاربر", "لطفا نام خود را وارد کنید:")
    if not name:
        messagebox.showwarning("خطا", "نام کاربر وارد نشده است.")
        return

    today_persian = datetime.now().strftime("%Y/%m/%d")
    title_default = "یک روز در مدرسه"

    prompt = f"سلام برادر {name}، امروز در تاریخ {today_persian}، چه خاطره‌ای داری؟\n"
    prompt += f"عنوان (مثلا '{title_default}') را وارد کن:"
    title = simpledialog.askstring("عنوان خاطره", prompt)
    if not title:
        title = title_default

    def ask_multiline_text():
        text_win = tk.Toplevel(root)
        text_win.title("متن خاطره")
        text_win.geometry("600x300")
        text_win.resizable(False, False)
        
        label = tk.Label(text_win, text="متن خاطره را وارد کنید (حدود 5-6 خط):", font=("Arial", 12))
        label.pack(pady=(10, 5))
        
        text_box = tk.Text(text_win, width=70, height=10, font=("Arial", 12))
        text_box.pack(padx=10, pady=(0, 10))
        text_box.focus()

        btn_frame = tk.Frame(text_win)
        btn_frame.pack(pady=(0, 15))

        result = {"text": None}

        def on_submit():
            content = text_box.get("1.0", tk.END).strip()
            if not content:
                messagebox.showwarning("خطا", "متن خاطره نمی‌تواند خالی باشد!")
                return
            result["text"] = content
            text_win.destroy()

        submit_btn = tk.Button(btn_frame, text="ثبت", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", command=on_submit)
        submit_btn.pack()

        root.wait_window(text_win)
        return result["text"]

    content_text = ask_multiline_text()
    if not content_text:
        return

    content = f"{today_persian}\n{name}\n{content_text}"

    save_note(name, title, content)
    root.mainloop()

if __name__ == "__main__":
    main()
