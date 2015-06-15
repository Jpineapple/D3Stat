import Tkinter
from compound_widgets import *
from DataController import *

class Win(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.stats_frame = Tkinter.Frame(self)
        self.stats_frame.pack(side="left", fill="both", expand=1)
            
        DataControl = DataController()
        labent_data = DataControl.gui_data()
        self.entry_store = []
        for i, k in enumerate(labent_data):
            label, col, row = k
            temp = LabelEntry(self.stats_frame, label, col, row)
            self.entry_store.append(temp)

        self.res = Tkinter.Frame(self)
        self.res.pack(side="left", fill="y", expand=1)
        
        self.button = Tkinter.Button(self.res, text="calculate",
                                     command=self.callback)
        self.button.pack(side="bottom")
        
    def callback(self):
        self.entrylist = {}
        for i, k in enumerate(self.entry_store):
            try:
                int(k.entryvar.get())
                self.entrylist[k.label.text] = k.entryvar.get()
            except:
                print "ERROR: Value for " + k.label.text + " not set."
        print self.entrylist
        
if __name__ == "__main__":
    app = Win(None)
    app.title("Diablo?!?")
    app.mainloop()
    
