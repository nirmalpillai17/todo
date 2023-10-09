import customtkinter as ctk
import tkinter as tk
from utils.constants import *
from utils.events import *

from widgets.button import StyledButton
from widgets.check_box import StyledCheckBox

from utils.text_wrap import break_sentence


class CardFrame(ctk.CTkFrame):
    def __init__(
            self,
            master,
            note,
            time,
            fg_color=COLOR_SET,
            **kwargs,
    ):
        super().__init__(
            master,
            fg_color=fg_color,
            border_width=2,
            border_color=BORDER_COLOR,
            corner_radius=0,
            **kwargs,
        )

        # format text to wrap on line break
        self.note = break_sentence(note, 60)

        # create button to remove task
        self.btn_remove = StyledButton(
            self,
            text="\u00D7",
            width=45,
            height=45,
            command=self.remove_instance,
        )
        self.btn_remove.pack(side=tk.LEFT, padx=20, pady=20)

        # create label to display task
        self.task_label = ctk.CTkLabel(
            self,
            text=self.note,
            font=CALB_22,
            justify=tk.LEFT,
        )
        self.task_label.pack(
            fill=tk.BOTH,
            side=tk.LEFT,
            pady=20,
            ipadx=15,
            ipady=20,
            expand=True,
        )

        # create checkbox to mark task as done
        self.cb_done = StyledCheckBox(
            self,
            text="",
            single_click=True,
            command=self.mark_as_done,
        )
        self.cb_done.pack(side=tk.LEFT, padx=20, pady=20)

    # method to remove a task card
    def remove_instance(self):
        self.pack_forget()
        self.destroy()
    
    # convert task text to strikethrough
    def mark_as_done(self):
        self.task_label.configure(
            font=("Calibri", 22, "bold", "overstrike"),
        )
