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
from color_config import read_config, save_config

class RunView:

    def __init__(self, gui, file_path):
        self.gui = gui
        self.file_path = file_path
        self.run_status = 0

        self.input_ready = False
        self.accept_input = False
        self.current_input = 'DEFAULT NO VALUE YET'
    
        self.file_window = tk.Toplevel(self.gui.root)
        self.file_window.geometry("800x500")
        
        self.primary_color_widgets = []
        self.secondary_color_widgets = []

        self.init_run_frame()
        self.init_view_frame()

        self.show_run()

    def init_run_frame(self):
        # Create the run frame with a green background
        self.run_frame = tk.Frame(self.file_window, bg=self.gui.primary_color)
        self.gui.primary_color_widgets.append(self.run_frame)
        self.primary_color_widgets.append(self.run_frame)
        self.run_status_bar(self.run_frame)
        self.output_console(self.run_frame)
        self.init_input(self.run_frame)

    def init_view_frame(self):
        #create the view frame
        self.view_frame = tk.Frame(self.file_window, bg=self.gui.primary_color)
        self.gui.primary_color_widgets.append(self.view_frame)
        self.primary_color_widgets.append(self.view_frame)
        self.view_status_bar(self.view_frame)
        self.view_text_editor(self.view_frame)

    def show_view(self):
        self.view_frame.pack(expand=True, fill=tk.BOTH)
        self.run_frame.pack_forget()

    def show_run(self):
        self.run_frame.pack(expand=True, fill=tk.BOTH)
        self.view_frame.pack_forget()
    
    def close(self):
        for item in self.primary_color_widgets:
            self.gui.primary_color_widgets.remove(item)
        for item in self.secondary_color_widgets:
            self.gui.secondary_color_widgets.remove(item)
        self.file_window.destroy()

    #run frame section
    def run_status_bar(self, target_window): 
        trimmed_name = (re.search("([^\\/]+)$", self.file_path)).group()       
        self.status_frame = tk.Frame(target_window, bg=self.gui.widget_bg)

        #use column structure for placing elements
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(1, weight=6)
        self.status_frame.columnconfigure(2, weight=1)
        self.status_frame.columnconfigure(3, weight=1)

        self.close_button = tk.Button(self.status_frame, text="Close", font=('Arial', 18), bg=self.gui.button_bg,
                                     command=self.close)
        self.file_name_label = tk.Label(self.status_frame, text=trimmed_name, font=('Arial', 18), wraplength=400, bg=self.gui.widget_bg,
                                         fg=self.gui.widget_fg)
        self.view_file_button = tk.Button(self.status_frame, text="View file", font=('Arial', 18), bg=self.gui.button_bg,
                                          command=self.show_view)
        self.run_button = tk.Button(self.status_frame, text="Run", font=('Arial', 18), command=self.run_file,
                                     bg=self.gui.secondary_color, foreground=self.gui.highlight_button_fg)
        self.gui.secondary_color_widgets.append(self.run_button)
        self.secondary_color_widgets.append(self.run_button)

        #place each element onto grid
        self.close_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5, pady=5)
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
        
        frame = tk.Frame(target_frame, width=300, height=200, bg=self.gui.widget_bg)
        frame.pack(expand=True, fill=tk.BOTH, padx=10)
        
        self.canvas = tk.Canvas(frame, bg="black", width=300, height=200, highlightthickness=0)
        self.canvas.bind("<MouseWheel>", on_mousewheel)
        
        vbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.canvas.yview, elementborderwidth=0)
        vbar.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        self.canvas.config(yscrollcommand=vbar.set)
        
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

        self.curr_line = 1
        self.o_font_size = 15
        self.labels = []
        trimmed_name = (re.search("([^\\/]+)$", self.file_path)).group()
        self.display_output("Run or view file {}".format(trimmed_name))

    def init_input(self, target_frame):
        self.input_frame = tk.Frame(target_frame, bg=self.gui.widget_bg)
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(0, weight=1)

        self.input_text = tk.Text(self.input_frame, height='2',font=('Arial', 16), background="gray70")
        self.input_text.grid(row=0, column=0, padx=5, pady=5)
        self.input_text.bind("<Return>", self.btn_input_press)

        self.input_button = tk.Button(self.input_frame, text="Enter", font=('Arial', 18),
                                      command=self.btn_input_press, background=self.gui.button_bg)
        self.input_button.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)

        self.input_frame.pack(fill='x', padx=10, pady=10)
    
    def prime_input(self):
        self.accept_input = True
        #print(f"{self}now accepting input")

    def get_input(self):
        if self.input_ready == True:
            self.input_ready = False
            return self.current_input
        else:
            return False
    
    def btn_input_press(self, event = 1):
        input = self.input_text.get('1.0', tk.END).strip()  # Capture input
        self.input_text.delete('0.0', tk.END)  # Clear the input field\
        if self.accept_input == True:
            self.accept_input = False
            self.current_input = input
            self.display_output(self.current_input)
            #print(f"{self}: input received {input}")
            self.input_ready = True
        else:
            self.display_output("input not accepted at this time")
        return "break"
    
    def toggle_run(self, errors = False):
        trimmed_name = (re.search("([^\\/]+)$", self.file_path)).group()
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
        self.toggle_run()
        def process_file():
            try:
                memory = Memory()
                ReadFile.read_file_to_memory(memory, self.file_path)
                Processor.process(memory, self)
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

    def view_status_bar(self, target_window): 
        trimmed_name = (re.search("([^\\/]+)$", self.file_path)).group()       
        self.status_frame = tk.Frame(target_window, bg=self.gui.widget_bg)

        #use column structure for placing elements
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(1, weight=6)
        self.status_frame.columnconfigure(2, weight=1)
        self.status_frame.columnconfigure(3, weight=1)

        self.close_window_button = tk.Button(self.status_frame, text="Close Window", font=('Arial', 18), bg=self.gui.button_bg,
                                     command=self.close)
        self.edit_file_name_label = tk.Label(self.status_frame, text=f'Editing: {trimmed_name}', font=('Arial', 18), wraplength=400, bg=self.gui.widget_bg,
                                         fg=self.gui.widget_fg)
        self.cancel_button = tk.Button(self.status_frame, text="Cancel", font=('Arial', 18), bg=self.gui.button_bg,
                                          command=self.show_run)
        self.save_button = tk.Button(self.status_frame, text="Save", font=('Arial', 18), command=self.save_file,
                                     bg=self.gui.secondary_color, foreground=self.gui.highlight_button_fg)
        self.gui.secondary_color_widgets.append(self.save_button)
        self.secondary_color_widgets.append(self.save_button)

        #place each element onto grid
        self.close_window_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5, pady=5)
        self.edit_file_name_label.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)
        self.cancel_button.grid(row=0, column=2, sticky=tk.W+tk.E, padx=5, pady=5)
        self.save_button.grid(row=0, column=3, sticky=tk.W+tk.E, padx=5, pady=5)

        self.status_frame.pack(fill='x', padx=10, pady=10)

    def check_file(self):
        lines = self.file_content.get(1.0, "end-1c").split("\n")
        regex_4 = r'^[+-]\d{4}$'
        regex_6 = r'^[+-]\d{6}$'
        i = 1
        if bool(re.match(regex_4, lines[0])) == True:
            for line in lines:
                line = line.strip()
                if bool(re.match(regex_4, line)) == True:
                    pass
                else:
                    messagebox.showerror("Error", 'SyntaxError: Line {}, "{}"'.format(i, line))
                    return False
                i+=1
            return True
        elif bool(re.match(regex_6, lines[0])) == True:
            for line in lines:
                line = line.strip()
                if bool(re.match(regex_6, line)) == True:
                    pass
                else:
                    messagebox.showerror("Error", 'SyntaxError: Line {}, "{}"'.format(i, line))
                    return False
                i+=1
            return True
        else:
            messagebox.showerror("Error", 'SyntaxError')
            return False

    def save_file(self):
        status = self.check_file()
        if status == True:
            new_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if new_file_path:
                lines = self.file_content.get(1.0, "end-1c").split("\n")
                self.file_path = new_file_path
                f = open(self.file_path, "w")
                for i in range(len(lines)):
                    f.write(lines[i])
                    if (i+1) != len(lines):
                        f.write("\n")


                #update file name headers
                trimmed_name = (re.search("([^\\/]+)$", self.file_path)).group() 
                self.file_name_label.config(text=trimmed_name)
                self.edit_file_name_label.config(text=trimmed_name)
                self.file_window.update_idletasks()
                self.show_run()
                f.close()
                messagebox.showinfo("File", "File saved")
            else:
                print("error getting save filepath")
        elif status == False:
            print("save aborted: syntax error")
    
    def check_250(self, event):
        lines = self.file_content.get(1.0, "end-1c").split("\n")
        if len(lines) > 250:
            messagebox.showerror("Error", 'Cannot exceed 250 lines')
            self.file_content.delete('251.0', 'end')
            return 'break'

    def view_text_editor(self, target_window):
        self.text_edit_frame = tk.Frame(target_window, bg=self.gui.widget_bg)
        self.file_content = tk.Text(self.text_edit_frame,height='110', highlightthickness=5, highlightbackground = self.gui.widget_bg, highlightcolor=self.gui.widget_bg)
        self.file_content.pack(fill=tk.BOTH, expand=True)
        
        self.file_content.bind("<Key>", self.check_250)
        try:
            with open(self.file_path, 'r') as f:
                self.file_content.insert(tk.END, f.read())
        except FileNotFoundError:
            self.file_content.insert(tk.END, "File not found")
        except Exception as e:
            self.file_content.insert(tk.END, f"An error occurred: {str(e)}")

        self.text_edit_frame.pack(fill='x', padx=10, pady=(0, 10))