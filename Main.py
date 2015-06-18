import Tkinter
from tkFileDialog import askopenfilename
from compound_widgets import *
from DataController import *

class Win(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        
    def initialize(self):
        self.damage_frame = Tkinter.Frame(self)
        self.damage_frame.pack(side="left", fill="both", expand=1, padx=10)
        
        self.dmglabel = Tkinter.Label(self.damage_frame, text="Damage Range")
        self.dmglabel.grid(column=0, row=0, columnspan=2)
        self.dmgmin = LabelEntry(self.damage_frame, "Min", 0, 1, width=10)
        self.dmgmax = LabelEntry(self.damage_frame, "Max", 1, 1, width=10)
        
        self.stats_frame = Tkinter.Frame(self)
        self.stats_frame.pack(side="left", fill="both", expand=1)
            
        DataControl = DataController()
        labent_data = DataControl.gui_data()
        self.entry_store = []
        for i, k in enumerate(labent_data):
            label, col, row = k
            temp = LabelEntry(self.stats_frame, label, col, row, width=len(label))
            self.entry_store.append(temp)
                    
        self.res = Tkinter.Frame(self)
        self.res.pack(side="left", fill="y", expand=1)
        
        self.button = Tkinter.Button(self.res, text="calculate",
                                     command=self.callback)
        self.button.pack(side="bottom")
        
        self.menubar = Tkinter.Menu(self)
        self.menubar.add_command(label="Open", command=self.get_file)
        self.menubar.add_command(label="Save", command=self.save_file)
        
        self.config(menu=self.menubar)
    
    def update_state(self):
        self.entry_state = {}
        for i, k in enumerate(self.entry_store):
            try:
                self.entry_state[k.label.text] = float(k.entryvar.get())
            except:
                print "ERROR: Value for " + k.label.text + " not set."
    
    def get_file(self):
        self.filename = askopenfilename()
        recons = {}
        with open(self.filename) as infile:
            for line in infile.readlines():
                k , v = line.split(":")
                recons[k.strip("''")] = v.strip()
        print recons
        
        for i, k in enumerate(self.entry_store):
            try:
                k.entryvar.set(float(recons[k.label.text]))
            except:
                continue
                
    def save_file(self):
        self.update_state()
        self.sav = str(self.entry_state)[1:-1]
        with open("D3Save.txt", "w+") as f:
            for line in self.sav.split(", "):
                f.write(line + "\n")
     
    def callback(self):
        self.update_state()
        print str(self.entry_state)
    
if __name__ == "__main__":
    app = Win(None)
    app.title("Diablo?!?")
    app.mainloop()
    
