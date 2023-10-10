import customtkinter as ctk
import tkinter as tk

from utils.constants import *


class StyledTab(ctk.CTkTabview):
    def __init__(self, master, fg_color=COLOR_SET, **kwargs):
        super().__init__(
            master=master,
            fg_color=fg_color,
            corner_radius=0,
            **kwargs,
        )

        # Accessing a private variable,
        # not a recommended practice!
        self._segmented_button.configure(
            font=CALB_16,
            border_width=10,
            selected_color=BTN_COLOR,
            selected_hover_color=BTN_COLOR_HOVER,
        )
