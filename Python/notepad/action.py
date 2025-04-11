from GetAndSet import var
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
        file1 = filedialog.askopenfile()
        for lines in file1:
            text.insert(1, lines)
            
          

