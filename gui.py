#gui will be updated to only perform its core responsibilities
#gui home is responsible for selecting a valid file and changing colors now, everything else goes

#gui will be updated to only perform its core responsibilities
#gui home is responsible for selecting a valid file and changing colors now, everything else goes

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
from gui_run_file import RunView

class GUI:
    from gui_view_file import view_file

    def __init__(self):

        #initialize color scheme
        saved_colors = read_config()
        self.primary_color = saved_colors[0]
        self.secondary_color = saved_colors[1]
        self.widget_bg = 'gray20'
        self.widget_fg = 'gray90'
        self.button_bg = "gray70"
        self.highlight_button_fg = 'white'
        self.primary_color_widgets = []
        self.secondary_color_widgets = []
        
        #class variables
        self.run_status = 0
        self.file_path = ''

        #create tkinter root window
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.minsize(500,400)
        self.root.title("UVSim Team E")
        self.root.configure(bg=self.primary_color)
        self.primary_color_widgets.append(self.root)

        # Initialize UI frame
        self.init_select_file()
        self.init_color_menu()
        self.root.mainloop()

    def get_file(self, new_path = False):
        if new_path == False:
            file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        else:
            file_path = new_path
        if file_path != '':
            trimmed_name = (re.search("([^\\/]+)$", file_path)).group()
            file_name = f'Selected file: {trimmed_name}'
            new_file_view = RunView(self, file_path)

    def init_select_file(self):
        self.status_frame = tk.Frame(self.root, bg=self.widget_bg)
        self.select_file_label = tk.Label(self.status_frame, text='Welcome to UVSIM! Select a file to start', font=('Arial', 20), bg=self.widget_bg,
                                         fg=self.widget_fg)
        
        self.select_file_button = tk.Button(self.status_frame, text="Select file", font=('Arial', 18),
                                          command=self.get_file, background=self.secondary_color, fg=self.highlight_button_fg)
        self.secondary_color_widgets.append(self.select_file_button)
        
        self.select_file_label.pack(anchor='w', padx=5, pady=5)
        self.select_file_button.pack(anchor='w', padx=5, pady=5)
        self.status_frame.pack(fill='x', padx=10, pady=10)

    def init_color_menu(self):

        self.color_menu_frame = tk.Frame(self.root, bg=self.widget_bg)
        self.color_label = tk.Label(self.color_menu_frame, text='Color Options:', font=('Arial', 16), wraplength=400, bg=self.widget_bg,
                                         fg=self.widget_fg, anchor='w')
        self.color_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.color_menu_frame.columnconfigure(0, weight=1)
        self.color_menu_frame.columnconfigure(1, weight=1)
        self.color_menu_frame.columnconfigure(2, weight=20)

        self.reset_colors_button = tk.Button(self.color_menu_frame, text="Reset", font=('Arial'),
                                                  command=self.reset_colors, background=self.button_bg)
        self.change_main_color_button = tk.Button(self.color_menu_frame, text="Background Color", font=('Arial'),
                                                  command=self.change_main_color, background=self.button_bg)
        self.change_secondary_color_button = tk.Button(self.color_menu_frame, text="Button Color", font=('Arial'),
                                                       command=self.change_secondary_color, background=self.button_bg)
        
        self.change_main_color_button.grid(row=1, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.change_secondary_color_button.grid(row=1, column=1, sticky=tk.W + tk.E, padx=5, pady=5)
        self.reset_colors_button.grid(row=2, column=0, sticky=tk.W + tk.E, padx=5, pady=5)

        self.color_menu_frame.pack(fill=tk.X, padx=10, pady=5)

    def reset_colors(self):
        default_primary = '#FFFFFF'
        default_secondary = '#4C721D'
        self.primary_color = default_primary
        self.secondary_color = default_secondary
        for widget in self.primary_color_widgets:
                widget.configure(bg=self.primary_color)
        for widget in self.secondary_color_widgets:
                widget.configure(bg=self.secondary_color)
        save_config(self.primary_color, self.secondary_color)
        self.root.update_idletasks()
    
    def change_main_color(self):
        color_info = colorchooser.askcolor(title="Choose BG Color")
        if color_info[1]:
            self.primary_color = color_info[1]
            for widget in self.primary_color_widgets:
                widget.configure(bg=self.primary_color)
            save_config(self.primary_color, self.secondary_color)
            self.root.update_idletasks()

    def change_secondary_color(self):
        color_info = colorchooser.askcolor(title="Choose Button Color")
        if color_info[1]:
            self.secondary_color = color_info[1]
            for widget in self.secondary_color_widgets:
                widget.configure(bg=self.secondary_color)
            save_config(self.primary_color, self.secondary_color)
            self.root.update_idletasks()