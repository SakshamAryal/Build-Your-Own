from tkinter import *
def create_widget(parent, widget_type, **option):
        return widget_type(parent,**option)

root = create_widget(None, Tk)
enter_text = create_widget(root, Frame)
text = create_widget(enter_text, Text)
ribbon = create_widget(root,Frame, height = 20,width = 700 ,background = 'red')
        
class var():

    def set_root(**option):
         root.config()
         

    def get_root():
         return root
    
    def get_entertext():
         return enter_text

    def get_text():
         return text
 
    def get_ribbon():
         return ribbon