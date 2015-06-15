#Compound Widgets
# cd C:\git\D3stat
import Tkinter


class LabelEntry(Tkinter.Tk):    
    def __init__(self, parent, label, column=0, row=0, entrydef="Set"):
        self.parent = parent
        self.container(parent, column, row)
        self.gen_label(parent, label, column, row)
        self.gen_entry(parent, column, row, entrydef)
        
    def container(self, parent, column, row):
        self.container = Tkinter.Frame(parent)
        self.container.grid(column=column, row=row)
        
    def gen_label(self, parent, label, column, row):
        self.label = Tkinter.Label(self.container, text=label)
        self.label.pack(side="top", fill="both", expand=1)
        
    def gen_entry(self, parent, column, row, entrydef):
        self.entryvar = Tkinter.StringVar(value=entrydef)
        self.entry = Tkinter.Entry(self.container, bg="yellow", textvariable=self.entryvar)
        self.entry.pack(side="top", fill="both", expand=1)
        
        self.entry.bind("<Button-1>", lambda event, v=self.entryvar: self.onclick(event, v))

    def onclick(self, event, var):
        self.entryvar.set("")
        
