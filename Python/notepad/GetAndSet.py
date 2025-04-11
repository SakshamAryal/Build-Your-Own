from tkinter import *

def create_widget(parent, widget_type, **option):
        return widget_type(parent,**option)

root = create_widget(None, Tk)
enter_text = create_widget(root, Frame)
text = create_widget(root, Text)
menubar = create_widget(root, Menu)
file_menu = create_widget(menubar, Menu, tearoff = 0)
class var:
    def set_root(tkinter):
         root = tkinter
         
    def set_MenuBar(Menu):
         menubar = Menu

    def set_text(Text):
         text = Text

    def set_FileMenu(Menu):
         file_menu = Menu

    def get_FileMenu():
         return file_menu
    
    def get_root():
         return root
    
    def get_entertext():
         return enter_text
    
    def get_text():
         return text
 
    def get_MenuBar():
         return menubar