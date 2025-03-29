from tkinter import *
from gui import gui_struct
from GetAndSet import var

instance_gui = gui_struct()
instance_gui._init_()



app = var.get_root()
app.mainloop()
 