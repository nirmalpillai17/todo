import customtkinter as ctk
import tkinter as tk
from utils.constants import *
from utils.events import *

from widgets.card import CardFrame


class StyledScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, fg_color=COLOR_SET, **kwargs):
        super().__init__(
            master=master,
            fg_color=fg_color,
            corner_radius=0,
            **kwargs,
        )

        # configure grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=1)

        self.card_list = ctk.CTkFrame(
            master=self,
            fg_color=COLOR_SET,
            corner_radius=0,
        )
        self.card_list.grid(column=1, sticky='nsew')

    def add_note_card(self, note, time):
        card_frame = CardFrame(self.card_list, note, time)
        card_frame.pack(pady=10, fill=tk.BOTH)
        card_frame.set_wordwrap()
