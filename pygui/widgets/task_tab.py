import customtkinter as ctk
import tkinter as tk

import requests
import json

from utils.constants import *

from widgets.scroll_frame import StyledScrollFrame
from widgets.button import StyledButton


# main application class
class TasksTab(ctk.CTkFrame):
    def __init__(self, master, fg_color=COLOR_SET, **kwargs):
        super().__init__(
            master=master,
            fg_color=fg_color,
            corner_radius=0,
            **kwargs,
        )

        # configure grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)

        # create note input box
        self.note = tk.StringVar()
        self.inp_box = ctk.CTkEntry(
            self,
            textvariable=self.note,
            height=45,
            width=45,
            font=CALB_22,
            corner_radius=0,
        )
        self.inp_box.grid(row=0, column=1, sticky='ew')

        # create add button
        self.btn_sub = StyledButton(
            self,
            text="+",
            command=self.add_task,
        )
        self.btn_sub.grid(row=0, column=2, sticky='w', padx=5)

        # create clear button
        self.btn_clear = StyledButton(
            self,
            text="\u00D7",
            command=self.clear_text,
        )
        self.btn_clear.grid(row=0, column=0, sticky='e', padx=5)

        # create scroll frame for task cards
        self.tasks_frame = StyledScrollFrame(self)
        self.tasks_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')
        
        self.tasks_frame.load_cards()

    def add_task(self):
        if self.note.get():
            self.tasks_frame.add_note_card(self.note.get(), UNDONE)
        self.clear_text()

    def clear_text(self):
        self.inp_box.delete(first_index=0, last_index=tk.END)
