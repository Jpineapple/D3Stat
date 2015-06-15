#Compound Widgets
import Tkinter


class LabelEntry(Tkinter.Tk):    
    def __init__(self, parent, label, column=0, row=0, entrydef="Set"):
        self.parent = parent
        self.entrydef = entrydef
        self.container(parent, column, row)
        self.gen_label(parent, label)
        self.gen_entry(parent, entrydef)
        
    def container(self, parent, column, row):
        self.container = Tkinter.Frame(parent)
        self.container.grid(column=column, row=row)
        
    def gen_label(self, parent, label):
        self.label = Tkinter.Label(self.container, text=label)
        self.label.text = label
        self.label.pack(side="top", fill="both", expand=1)
        
    def gen_entry(self, parent, entrydef):
        self.entryvar = Tkinter.StringVar(value=entrydef)
        self.entry = Tkinter.Entry(self.container, bg="yellow", textvariable=self.entryvar)
        self.entry.pack(side="top", fill="both", expand=1)
        
        self.entry.bind("<Button-1>", self.onclick)
        self.entry.bind("<FocusOut>", self.onleave)

    def onclick(self, event):
        try:
            int(event.widget.get())
        except:
            self.entryvar.set("")
        
    def onleave(self, event):
        if self.entry.get() is "":
            self.entryvar.set(self.entrydef)
