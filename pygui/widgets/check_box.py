import customtkinter as ctk
import tkinter as tk
from utils.constants import *
from utils.events import *

class StyledCheckBox(ctk.CTkCheckBox, EventHandler):
   def __init__(self, master, command, width=45,
                height=45, single_click=True, **kwargs):

      super().__init__(
         master=master,
         width=width,
         height=height,
         fg_color=BTN_COLOR,
         hover_color=BTN_COLOR_HOVER,
         command=self.cmd_wrapper,
         corner_radius=0,
         **kwargs,
      )

      self.sc = single_click
      self.func = command

   # disable the checkbox after first click
   # in case single_click is set to True
   def cmd_wrapper(self):
      if self.sc:
         self.configure(fg_color=BTN_COLOR_HOVER, state=tk.DISABLED)
      self.func()
      return
