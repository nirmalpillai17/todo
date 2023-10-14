import customtkinter as ctk
import tkinter as tk
from utils.constants import *
from utils.events import *

from utils.request import send_request 
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

    def add_note_card(self, note, status):
        data = {'note':note, 'status':status}
        id = send_request("http://localhost:8080/todo/nr", "POST", data)
        card_frame = CardFrame(self.card_list, note, status, id)
        card_frame.pack(pady=10, fill=tk.BOTH)
        card_frame.set_wordwrap()

    def load_cards(self):
        data = send_request("http://localhost:8080/todo/gr", "GET")
        for field in data:
            details = data[field]
            card_frame = CardFrame(
                self.card_list,
                details["note"],
                details["status"],
                field,
            )
            card_frame.pack(pady=10, fill=tk.BOTH)
            card_frame.set_wordwrap()
             
