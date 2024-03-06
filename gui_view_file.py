import tkinter as tk

def view_file(self):
    file_name = self.file_path
    self.file_view = tk.Toplevel(self.root)
    self.file_view.title(file_name)
    self.file_view.geometry("800x500")

    self.file_content = tk.Text(self.file_view)
    self.file_content.pack(fill=tk.BOTH, expand=True)

    try:
        with open(file_name, 'r') as f:
            self.file_content.insert(tk.END, f.read())
    except FileNotFoundError:
        self.file_content.insert(tk.END, "File not found")
    except Exception as e:
        self.file_content.insert(tk.END, f"An error occurred: {str(e)}")
