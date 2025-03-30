from GetAndSet import var
from tkinter import filedialog

class act:
    def saveas():
            text = var.get_text()
            t = text.get("1.00", "end-1c")
            savelocation = filedialog.asksaveasfilename()
            file1  = open(savelocation, "w+")
            file1.write(t)
            file1.close()
