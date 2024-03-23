import tkinter as tk
from tkinter import messagebox
import re

def view_file(self):
    def check_file():
        lines = self.file_content.get(1.0, "end-1c").split("\n")
        regex = r'^[+-]\d{1,4}$'
        i = 1
        for line in lines:
            line = line.strip()
            if bool(re.match(regex, line)) == True:
                pass
            else:
                messagebox.showerror("Error", 'SyntaxError: Line {}, "{}"'.format(i, line))
                return False
            i+=1
        return True

    def save_file():
        status = check_file()
        if status == True:
            print("ready to save")
        elif status == False:
            print("bad syntax")

    def cancel():
        self.file_view.destroy()

    def on_key_press(event):
        lines = self.file_content.get(1.0, "end-1c").split("\n")
        if len(lines) > 100:
            messagebox.showerror("Error", 'Cannot exceed 100 lines')
            self.file_content.delete('101.0', 'end')
            return 'break'

    file_name = self.file_path
    self.file_view = tk.Toplevel(self.root)
    self.file_view.title(file_name)
    self.file_view.geometry("800x500")

    self.save_file_button = tk.Button(self.file_view, text="Save", font=('Arial', 18),
                                          command=save_file, background="gray70")

    self.cancel_button = tk.Button(self.file_view, text="Cancel", font=('Arial', 18),
                                          command=cancel, background="gray70")
    
    self.save_file_button.pack()
    self.cancel_button.pack()
    self.file_content = tk.Text(self.file_view,height='110')
    self.file_content.pack(fill=tk.BOTH, expand=True)
    
    self.file_content.bind("<Key>", on_key_press)

    try:
        with open(file_name, 'r') as f:
            self.file_content.insert(tk.END, f.read())
    except FileNotFoundError:
        self.file_content.insert(tk.END, "File not found")
    except Exception as e:
        self.file_content.insert(tk.END, f"An error occurred: {str(e)}")