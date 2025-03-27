from GetAndSet import var
from tkinter import *
class gui_struct():
    def Ribbon(self):
        rib = var.get_ribbon()
    
    def Root(self):
        app = var.get_root()
        app.title("Build your own Notepad")
        var.set_root(app)
    
    def _init_(self):
        self.Root()
        self.Ribbon()
        
    
        
