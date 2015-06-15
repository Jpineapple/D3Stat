import Tkinter
from compound_widgets import *
from DataController import *

class Win(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.stats = Tkinter.Frame(self)
        self.stats.pack(side="left", fill="both", expand=1)
<<<<<<< HEAD:Test.py
         
        self.dex = LabelEntry(self.stats, "Dex", 0, 0)
        self.critc = LabelEntry(self.stats, "Crit Chance", 1, 0)
        self.critdmg = LabelEntry(self.stats, "Crit Damage", 1, 2)
        
=======
            
        DataControl = DataController()
        labent_data = DataControl.gui_data()
        for i, k in enumerate(labent_data):
            label, col, row = k
            LabelEntry(self.stats, label, col, row)
>>>>>>> Data-Entry-conf-file:Main.py
        
        self.res = Tkinter.Frame(self)
        self.res.pack(side="left", fill="y", expand=1)
        
<<<<<<< HEAD:Test.py
        self.button = Tkinter.Button(self.res, text="calculate", command=self.callback)
        self.button.pack(side="bottom")
        
    def callback(self):
        print self.dex.entryvar.get()
        print self.critc.entryvar.get()
        print self.critdmg.entryvar.get()
        
"""    
       
        self.resvar = Tkinter.StringVar()
        label = Tkinter.Label(self.res, textvariable=self.resvar)
        label.grid(column=0, row=0)
"""

=======
        self.results = ButtonResult(self.res)
>>>>>>> Data-Entry-conf-file:Main.py
    
        
        
if __name__ == "__main__":
    app = Win(None)
    app.title("Diablo?!?")
    app.mainloop()
    