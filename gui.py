import tkinter as tk
from tkinter import messagebox

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("UVSim Team E")

        #initialize ui frames
        self.init_menu()
        self.init_status()
        self.init_output()
        self.init_input()
        
        self.root.mainloop()
    
    def get_input(self):
        input = self.input_text.get('1.0', tk.END).strip()
        self.input_text.delete('1.0', tk.END)
        print("Input: {}".format(input))

    def get_file(self):
        print("Open file!")

    def run_file(self):
        print("Run file!")

    def init_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open File", command=self.get_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close", command=exit)

        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        self.root.config(menu=self.menu_bar)
    
    def init_status(self):
        self.status_frame = tk.Frame(self.root)
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(0, weight=1)
        
        self.file_name = 'file_name.txt'
        self.file_name_label = tk.Label(self.status_frame, text=self.file_name, font=('Arial', 18))
        self.file_name_label.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.run_button = tk.Button(self.status_frame, text="run", font=('Arial', 18), command=self.run_file)
        self.run_button.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.status_frame.pack(fill='x', padx=10, pady=10)

    def init_output(self):
        self.output_label = tk.Label(height='12', text="this is where output goes", font=('Arial', 18), 
                                     background="black", foreground="white")
        self.output_label.pack(fill='x', padx=10, pady=10)

    def init_input(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(0, weight=1)
        
        self.input_text = tk.Text(self.input_frame, height='2',font=('Arial', 16))
        self.input_text.grid(row=0, column=0)
        
        self.input_button = tk.Button(self.input_frame, text="enter", font=('Arial', 18), command=self.get_input)
        self.input_button.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.input_frame.pack(fill='x', padx=10, pady=10)