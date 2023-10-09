from .constants import *

class EventHandler:
    # event handler for hover
    def on_enter(self, e):
        self.configure(fg_color=BTN_COLOR_HOVER)

    # event handler for hover end
    def on_leave(self, e):
        self.configure(fg_color=BTN_COLOR)
