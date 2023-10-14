import customtkinter as ctk
import tkinter as tk
from utils.constants import *
from utils.events import *

from utils.request import send_request

from widgets.button import StyledButton
from widgets.check_box import StyledCheckBox


class CardFrame(ctk.CTkFrame):
    def __init__(self, master, note, status, id,
                 fg_color=COLOR_SET, **kwargs):

        super().__init__(
            master=master,
            fg_color=fg_color,
            border_width=2,
            border_color=BORDER_COLOR,
            corner_radius=0,
            **kwargs,
        )

        self.id = id
        self.note = note

        # create button to remove task
        self.btn_remove = StyledButton(
            master=self,
            text="\u00D7",
            width=45,
            height=45,
            command=self.remove_instance,
        )
        self.btn_remove.pack(side=tk.LEFT, padx=20, pady=20)

        # create label to display task
        self.task_label = ctk.CTkLabel(
            master=self,
            text=note,
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
            master=self,
            text='',
            command=self.mark_as_done,
            status=status,
        )
        self.cb_done.pack(side=tk.LEFT, padx=20, pady=20)

        if status == DONE:
            self.mark_as_done()

    # method to remove a task card
    def remove_instance(self):
        send_request(f"http://localhost:8080/todo/dr/{self.id}", "DELETE") 
        self.pack_forget()
        self.destroy()

    # convert task text to strikethrough
    def mark_as_done(self):
        data = {'note':self.note, 'status':0}
        send_request(f"http://localhost:8080/todo/ur/{self.id}", "PUT", data)
        self.task_label.configure(font=("Calibri", 22, "bold", "overstrike"))
        self.cb_done.set_disabled()

    # method to set word wrap for label
    def set_wordwrap(self):
        self.update_idletasks()
        self.task_label.configure(wraplength=self.winfo_width() * 0.8)
