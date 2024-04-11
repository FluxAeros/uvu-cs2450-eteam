#this contains the new window for the gui file view
#it will allow for the user to toggle between edit and run modes in the same contiguous window
#design spec in my notes
import re
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from memory import Memory
from processor import Processor
from read_file import ReadFile
from input_output import IO
from read_file import ReadFile
from gui_config import read_config, save_config

class FileView:

    def __init__(self, gui, file_path):
        self.gui = gui
        self.file_path = file_path
        self.run_status = 0
    
        self.primary_color_widgets = []
        self.secondary_color_widgets = []
        self.primary_color = '#4C721D'  # Dark green
        self.off_color = '#FFFFFF'  # White

        self.file_window = tk.Toplevel(self.gui.root)
        self.file_window.geometry("800x500")
        self.init_run_frame()
        self.init_view_frame()

        self.show_run()

    def init_run_frame(self):
        # Create the run frame with a green background
        self.run_frame = tk.Frame(self.file_window, bg="light green")
        self.run_status_bar(self.run_frame)
        self.output_console(self.run_frame)
        self.init_input(self.run_frame)

    def init_view_frame(self):
        #create the view frame
        self.view_frame = tk.Frame(self.file_window, bg="light blue")
        self.view_to_run_button = tk.Button(self.view_frame, text="View Button", command=self.show_run)
        self.view_to_run_button.pack()

    def show_view(self):
        self.view_frame.pack(expand=True, fill=tk.BOTH)
        self.run_frame.pack_forget()

    def show_run(self):
        self.run_frame.pack(expand=True, fill=tk.BOTH)
        self.view_frame.pack_forget()

    #run frame section
    def run_status_bar(self, target_window):        
        self.status_frame = tk.Frame(target_window, bg=self.primary_color)
        self.primary_color_widgets.append(self.status_frame)

        #use column structure for placing elements
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(1, weight=6)
        self.status_frame.columnconfigure(2, weight=1)
        self.status_frame.columnconfigure(3, weight=1)

        self.home_button = tk.Button(self.status_frame, text="Home", font=('Arial', 18), 
                                     command=lambda: print("gi go home"), bg='white', fg='black')
        self.file_name_label = tk.Label(self.status_frame, text="still need a name", font=('Arial', 18), wraplength=400, bg="white",
                                         fg="black")
        self.view_file_button = tk.Button(self.status_frame, text="View file", font=('Arial', 18),
                                          command=self.show_view, bg="white", fg="black")
        self.run_button = tk.Button(self.status_frame, text="Run", font=('Arial', 18), command=self.run_file,
                                     bg="purple", foreground='white')
        
        #place each element onto grid
        self.home_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5, pady=5)
        self.file_name_label.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)
        self.view_file_button.grid(row=0, column=2, sticky=tk.W+tk.E, padx=5, pady=5)
        self.run_button.grid(row=0, column=3, sticky=tk.W+tk.E, padx=5, pady=5)

        self.status_frame.pack(fill='x', padx=10, pady=10)

    def display_error(self, error_msg):
        error_txt = 'ERROR: ' + error_msg
        self.display_output(error_txt)

    def display_output(self, txt = ''):
        label = tk.Label(self.canvas, text=txt, font=('Arial', self.o_font_size), fg="gray85", bg="black",
                          anchor=tk.W, padx=5, pady=5)
        self.labels.append(label)
        self.canvas.create_window(0, self.curr_line * (self.o_font_size * 2), anchor=tk.NW, window=label)
        self.curr_line += 1
        
        # Update the scroll region and canvas height
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.canvas.yview_moveto(1)

    def output_console(self, target_frame):
        def on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        frame = tk.Frame(target_frame, width=300, height=200, bg="white")
        frame.pack(expand=True, fill=tk.BOTH, padx=10)
        self.secondary_color_widgets.append(frame)
        
        self.canvas = tk.Canvas(frame, bg="black", width=300, height=200, highlightthickness=0)
        self.canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        vbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.canvas.yview, elementborderwidth=0)
        vbar.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        self.canvas.config(yscrollcommand=vbar.set)
        
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

        self.curr_line = 1
        self.o_font_size = 15
        self.labels = []
        self.display_output("Please select a file")

    def init_input(self, target_frame):
        self.input_frame = tk.Frame(target_frame, bg="white")
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(0, weight=1)
        self.secondary_color_widgets.append(self.input_frame)

        self.input_text = tk.Text(self.input_frame, height='2',font=('Arial', 16), background="gray70")
        self.input_text.grid(row=0, column=0, padx=5, pady=5)
        self.input_text.bind("<Return>", self.get_input)

        self.input_button = tk.Button(self.input_frame, text="Enter", font=('Arial', 18),
                                      command=self.get_input, background="gray70")
        self.input_button.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

        self.input_frame.pack(fill='x', padx=10, pady=10)
    
    def get_input(self, event = 1):
        self.user_input = self.input_text.get('1.0', tk.END).strip()  # Capture input
        self.input_text.delete('0.0', tk.END)  # Clear the input field
        #self.display_output(GUI.user_input)
        IO.input_ready_event.set()
        return "break"
    
    def toggle_run(self, trimmed_name, errors = False):
        if self.run_status == 0:
            self.display_output(f"Running file {trimmed_name}")
            self.run_status = 1
            self.run_button.config(state=tk.DISABLED)
        elif(self.run_status == 1 and not(errors)):
            self.display_output(f"Finished running {trimmed_name}")
            self.run_status = 0
            self.run_button.config(state=tk.NORMAL)
        else:
            self.display_output(f"Terminated {trimmed_name} with errors")
            self.run_status = 0
            self.run_button.config(state=tk.NORMAL)
            
    def run_file(self):
        self.toggle_run('no file')
        def process_file():
            try:
                memory = Memory()
                ReadFile.read_file_to_memory(memory, self.file_path)
                Processor.process(memory, self)
                print("I made it!")
            except AttributeError:
                self.display_error("no file selected")
                self.toggle_run(True)
                raise AttributeError("no file selected")
            except FileNotFoundError:
                self.display_error("no file selected")
                self.toggle_run(True)
                raise FileNotFoundError("no file selected")
            except IndexError:
                self.display_error("Invalid memory location")
                self.toggle_run(True)
                raise IndexError("Invalid memory location")
            except ValueError:
                self.display_error("Invalid file")
                self.toggle_run(True)
                raise ValueError
            except:
                self.display_error("unknown")
                self.toggle_run(True)
                raise RuntimeError("unknown")

        processing_thread = threading.Thread(target=process_file)
        processing_thread.start()