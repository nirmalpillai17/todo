import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

from widgets.check_box import StyledCheckBox
from widgets.button import StyledButton
from widgets.scroll_frame import StyledScrollFrame
from widgets.tab import StyledTab
from widgets.task_tab import TasksTab

from utils.text_wrap import break_sentence

class ToDoApp(ctk.CTk):
   def __init__(self):
      super().__init__()

      # setup window
      self.geometry('850x600')
      self.title('To-Do using Go')

      self.columnconfigure(0, weight=1)
      self.columnconfigure(1, weight=4)
      self.columnconfigure(2, weight=1)

      self.rowconfigure(0, weight=1)

      self.tabs = StyledTab(self)
      self.task_tab = self.tabs.add("Tasks")
      self.notes_tab = self.tabs.add("Notes")
      self.tabs.grid(
         row=0,
         column=0,
         columnspan=3,
         sticky='nsew',
         pady=15,
      )

      self.task_tab.columnconfigure(0, weight=1)
      self.task_tab.rowconfigure(0, weight=1)

      self.task_window = TasksTab(self.task_tab)
      self.task_window.grid(row=0, column=0, sticky='nsew')

      # create theme button
      self.btn_theme = StyledButton(
         self,
         text="\u2600",
         command=self.theme_change,
      ) 
      self.btn_theme.grid(row=0, column=0, sticky='nw', padx=20, pady=20)

      # create refresh button
      self.btn_refresh = StyledButton(
         self,
         text="\u27F3",
      )
      self.btn_refresh.grid(row=0, column=2, sticky='ne', padx=20, pady=20)

   # method to change app theme
   def theme_change(self):
      if ctk.get_appearance_mode().lower() == 'dark':
         theme, icon = ('light', '\u263D')
      else:
         theme, icon = ('dark', '\u2600')
      
      ctk.set_appearance_mode(theme)
      self.btn_theme.configure(text=icon)


# run the application instance
instance = ToDoApp()
instance.mainloop()