from tkinter import *

def create_widget(parent, widget_type, **option):
        return widget_type(parent,**option)

root = create_widget(None, Tk)
text = create_widget(root, Text)
menubar = create_widget(root, Menu)
file_menu = create_widget(menubar, Menu, tearoff = 0)
file_name = create_widget(root, StringVar)
new_window = create_widget(root, Toplevel)
class var:

    def set_root(tkinter):
         root = tkinter
    def get_root():
         return root
    
    def set_MenuBar(Menu):
         menubar = Menu
    def get_MenuBar():
         return menubar
    
    def set_text(Text):
         text = Text
    def get_text():
         return text
    
    def set_FileMenu(Menu):
         file_menu = Menu
    def get_FileMenu():
         return file_menu
    
    def set_Filename(String):
         file_name.set(String)
    def get_Filename():
         return file_name.get()
    
    def set_NewWindow(Toplevel):
         new_window = to
    def get_NewWindow():
         return new_window