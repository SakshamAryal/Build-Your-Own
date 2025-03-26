from tkinter import *
from tkinter import filedialog

global text
class mainbody():

    def create_widget(parent, widget_type, **option):
        return widget_type(parent,**option)
    
    root = create_widget(None, Tk)
    root.title("Text Editor")
    root.geometry()

    height = root.winfo_height()
    enter_text = Frame(root)
    text = create_widget(enter_text, Text)

    enter_text.pack(fill = "both", pady = 50)

    text.pack(fill = "both", expand = 1)

    def saveas():
        t = text.get("1.00", "end-1c")
        savelocation = filedialog.asksaveasfilename()
        file1  = open(savelocation, "w+")
        file1.write(t)
        file1.close()

    ribbon = Frame(root, height = 20,width = 700 ,background = 'red')
    button = Button(ribbon, text="Save", command=saveas)

    button.grid()
    root.mainloop()


