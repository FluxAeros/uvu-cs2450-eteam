import re
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from memory import Memory
from processor import Processor
from read_file import ReadFile
from input_output import IO
from read_file import ReadFile

class GUI:
    user_input = ""

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("UVSim Team E")
        self.root.configure(bg="grey12")

        #initialize ui frames
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
        #trim filepath so it fits on the screen
        trimmed_name = (re.search("([^\\/]+)$", self.file_path)).group()
        self.file_name_label.config(text = f'Selected file: {trimmed_name}')
        if self.file_path:
            self.display_output(f"Successfully loaded '{trimmed_name}'")
        else:
            self.display_error("no file selected")

    def run_file(self):
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

    def init_status(self):
        self.status_frame = tk.Frame(self.root, bg="gray25")
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(1, weight=6)
        self.status_frame.columnconfigure(2, weight=1)
        
        self.open_file_button = tk.Button(self.status_frame, text="Select file", font=('Arial', 18), 
                                          command=self.get_file, background="gray70")
        self.open_file_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5, pady=5)

        self.file_name = 'Select a file to start'
        self.file_name_label = tk.Label(self.status_frame, text=self.file_name, font=('Arial', 18), wraplength=400, bg="gray25",
                                         foreground="gray80")
        self.file_name_label.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

        self.run_button = tk.Button(self.status_frame, text="Run", font=('Arial', 18), command=self.run_file, bg="darkgreen", foreground='gray80')
        self.run_button.grid(row=0, column=2, sticky=tk.W+tk.E, padx=5, pady=5)

        self.status_frame.pack(fill='x', padx=10, pady=10)

    def init_output(self):
        frame=tk.Frame(self.root,width=300,height=10000)
        frame.pack(expand=True, fill=tk.BOTH, padx=10)
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
        self.input_frame = tk.Frame(self.root, bg="gray25")
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(0, weight=1)

        self.input_text = tk.Text(self.input_frame, height='2',font=('Arial', 16), background="gray70")
        self.input_text.grid(row=0, column=0, padx=5, pady=5)

        self.input_button = tk.Button(self.input_frame, text="Enter", font=('Arial', 18),
                                      command=self.get_input, background="gray70")
        self.input_button.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

        self.input_frame.pack(fill='x', padx=10, pady=10)
