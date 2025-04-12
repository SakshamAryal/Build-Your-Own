from GetAndSet import var
from tkinter import *
from tkinter import filedialog
app = var.get_root()
text = var.get_text()
class act:
    
    def saveas():
        text = var.get_text()
        t = text.get("1.00", "end-1c")
        savelocation = filedialog.asksaveasfilename()
        file1  = open(savelocation, "w+")
        file1.write(t)
        file1.close()
    def open():
        filename = filedialog.askopenfilename(initialdir="/Documents/", title="Open a .txt file", filetypes= (("txt files", "*.txt"),))
        app.title(filename)
        var.set_root(app)
        file1 = open(filename)
        for lines in file1:
            text.insert(END, lines)
            
          

