from GetAndSet import var
from tkinter import *
from action import act

class gui_struct:
    def _init_(self) -> None:
        
        self.Text()
        self.Root() 
    
    # halfway done
    def Root(self):
        self.root = var.get_root()
        self.root.title("Build your own notepad")
        self.root.geometry("630x430")
        self.root.config(menu = self.MenuBar()) 
        var.set_root(self.root)
    
    def MenuBar(self):
        self.menubar = var.get_MenuBar()
        self.menubar.add_cascade(label = "File", menu = self.File_Menu())
        var.set_MenuBar(self.menubar)
        return self.menubar

    def File_Menu(self):
        self.menu = var.get_FileMenu()
        self.menu.add_command(label = "New Window", command = None)
        self.menu.add_command(label = "Open", command = act.open)
        self.menu.add_command(label = "Save", command = None)
        self.menu.add_command(label = "Save As", command = act.saveas)
        self.menu.add_command(label = "CLose", command = self.root.destroy)
        var.set_FileMenu(self.menu)
        return self.menu
    
    def Text(self):
        self.text = var.get_text()
        self.text.pack(fill = "both", expand = "true")
        var.set_text(self.text)