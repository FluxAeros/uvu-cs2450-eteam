import tkinter as tk
from tkinter import messagebox, filedialog
import re

def view_file(view_frame):
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
            new_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if new_file_path:
                lines = self.file_content.get(1.0, "end-1c").split("\n")
                self.get_file(new_file_path)
                f = open(self.file_path, "w")
                for i in range(len(lines)):
                    f.write(lines[i])
                    if (i+1) != len(lines):
                        f.write("\n")
                self.file_view.destroy()
                f.close()
                messagebox.showinfo("File", "File saved")
            else:
                print("error getting save filepath")
        elif status == False:
            print("save aborted: syntax error")

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

    self.save_cancel_bar = tk.Frame(self.file_view, bg=self.primary_color)
    self.primary_color_widgets.append(self.save_cancel_bar)
    self.save_cancel_bar.pack(fill='x', padx=10, pady=10)
    self.save_cancel_bar.columnconfigure(0, weight=1)
    self.save_cancel_bar.columnconfigure(1, weight=1)

    self.save_file_button = tk.Button(self.save_cancel_bar, text="Save", font=('Arial', 18),
                                          command=save_file, background="gray70")

    self.cancel_button = tk.Button(self.save_cancel_bar, text="Cancel", font=('Arial', 18),
                                          command=cancel, background="gray70")
    self.save_file_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5, pady=5)
    self.cancel_button.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)
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