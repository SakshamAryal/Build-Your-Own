from text_editor import text
from tkinter import filedialog

class act():
    def saveas():
            t = text.get("1.00", "end-1c")
            savelocation = filedialog.asksaveasfilename()
            file1  = open(savelocation, "w+")
            file1.write(t)
            file1.close()
