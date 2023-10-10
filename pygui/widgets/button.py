import customtkinter as ctk
from utils.constants import *
from utils.events import *


# custom button with common theme attributes
class StyledButton(ctk.CTkButton, EventHandler):
    def __init__(self, master, width=45,
                 height=45, font=CALB_22, **kwargs):

        super().__init__(
            master=master,
            width=width,
            height=height,
            fg_color=BTN_COLOR,
            font=font,
            border_width=2,
            border_color=BORDER_COLOR,
            corner_radius=0,
            **kwargs,
        )

        # bind the buttons to events
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
