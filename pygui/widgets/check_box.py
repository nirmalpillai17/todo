import customtkinter as ctk
import tkinter as tk
from utils.constants import *
from utils.events import *

class StyledCheckBox(ctk.CTkCheckBox, EventHandler):
   def __init__(self, master, command, status, 
                width=45, height=45, **kwargs):

      super().__init__(
         master=master,
         width=width,
         height=height,
         fg_color=BTN_COLOR,
         hover_color=BTN_COLOR_HOVER,
         command=command,
         corner_radius=0,
         **kwargs,
      )

      if status == DONE:
         self.set_disabled()

   def set_disabled(self):
      self.select()
      self.configure(fg_color=BTN_COLOR_HOVER, state=tk.DISABLED)

