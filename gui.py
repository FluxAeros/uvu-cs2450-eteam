import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading
from memory import Memory
from read_file import ReadFile
from processor import Processor
from input_output import IO

class GUI:

    user_input = ""

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
        GUI.user_input = self.input_text.get('1.0', tk.END).strip()  # Capture input
        self.input_text.delete('1.0', tk.END)  # Clear the input field
        self.display_output(GUI.user_input)
        IO.input_ready_event.set()

    def get_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        self.file_name_label.config(text = f'Selected file: {self.file_path}')
        f_path_steps = self.file_path.split('/')
        if self.file_path:
            self.display_output(f"Successfully loaded '{f_path_steps[-1]}'")
        else:
            self.display_error("no file selected")

    def run_file(self):
##        for i in range (1, 100, 3):
##            txt = 'x' * i
##            self.display_output(txt)
        def process_file():
            try:
                memory = Memory()
                ReadFile.read_file_to_memory(memory, self.file_path)
                Processor.process(memory, self)
            except AttributeError:
                self.display_error("no file selected")
            except FileNotFoundError:
                self.display_error("no file selected")
            except IndexError:
                self.display_error("Invalid memory location")

        processing_thread = threading.Thread(target=process_file)
        processing_thread.start()

    def init_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=exit)

        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        self.root.config(menu=self.menu_bar)

    def init_status(self):
        self.status_frame = tk.Frame(self.root)
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(0, weight=1)

        self.file_name = 'Selected file: file_name.txt'
        self.file_name_label = tk.Label(self.status_frame, text=self.file_name, font=('Arial', 18))
        self.file_name_label.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.open_file_button = tk.Button(self.status_frame, text="Select file", font=('Arial', 18), command=self.get_file)
        self.open_file_button.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.run_button = tk.Button(self.status_frame, text="run", font=('Arial', 18), command=self.run_file)
        self.run_button.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.status_frame.pack(fill='x', padx=10, pady=10)

    def init_output(self):
        frame=tk.Frame(self.root,width=300,height=10000)
        frame.pack(expand=True, fill=tk.BOTH)
        self.canvas=tk.Canvas(frame,bg="black",width=300,height=10000,scrollregion=(0,0,1000,10000))

        #scroll bar
        hbar=tk.Scrollbar(frame,orient=tk.HORIZONTAL)
        hbar.pack(side=tk.BOTTOM,fill=tk.X)
        hbar.config(command=self.canvas.xview)
        vbar=tk.Scrollbar(frame,orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT,fill=tk.Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(width=300,height=300)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

        self.curr_line = 1
        self.o_font_size = 12
        self.display_output("Please select a file")

    def display_output(self, txt):
        output_y = self.curr_line * (self.o_font_size * 1.5)
        output_x = 5
        self.curr_line += 1
        self.canvas.create_text(output_x, output_y, text=txt, font=('Arial', self.o_font_size),
                                fill="white", anchor = tk.SW)
        self.canvas.pack()
        if output_y >= 10000:
            self.canvas.delete("all")
            self.curr_line = 1
            self.display_output("Warning: Window reset due to size")

    def display_error(self, error_msg):
        error_txt = 'ERROR: ' + error_msg
        self.display_output(error_txt)

    def init_input(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(0, weight=1)

        self.input_text = tk.Text(self.input_frame, height='2',font=('Arial', 16))
        self.input_text.grid(row=0, column=0)

        self.input_button = tk.Button(self.input_frame, text="enter", font=('Arial', 18),
                                      command=self.get_input)
        self.input_button.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.input_frame.pack(fill='x', padx=10, pady=10)
