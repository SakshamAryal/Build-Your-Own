from GetAndSet import var
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
app = var.get_root()
input_text= var.get_text()
filename = None
class act:
    @classmethod
    def saveas(self):
        text = input_text.get("1.00", "end-1c")
        savelocation = filedialog.asksaveasfilename(defaultextension= ".txt", filetypes= (("Text Document", "*.txt"),))
        file1  = open(savelocation, "w+")
        file1.write(text)
        file1.close()
        app.title(savelocation)
        var.set_root(app)
    
    @classmethod
    def open(self):
        filename = filedialog.askopenfilename(initialdir="/Documents/", title="Open a .txt file", 
                                                filetypes= (("Text Document", "*.txt"),))
        try:
            file1 = open(filename)
        except FileNotFoundError:
            print("File not selected")
            return 1
        app.title(filename)
        var.set_root(app)
        print(filename)
        var.set_Filename(self,filename)
        input_text.delete(1.0, END)
        for lines in file1:
            input_text.insert(END, lines)
        file1.close()
        
    @classmethod
    def save(self):
        text = input_text.get("1.00", "end-1c")
        print(filename)
        if filename == None:
            answer = messagebox.askokcancel("File doesn't exist", 
                                            "Do you want to create a new file?")
            if answer == True:
                self.saveas()
        else:
            file1 = open(filename, "w+")
            file1.write(text)
            file1.close()
