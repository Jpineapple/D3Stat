#Compound Widgets
import Tkinter


class LabelEntry(Tkinter.Frame):    
    def __init__(self, parent, label, column=0, row=0, entrydef="Set", width=20):
        self.name = label
        self.entrydef = entrydef
        
        Tkinter.Frame.__init__(self, parent)
        self.grid(column=column, row=row)
        
        self.label = Tkinter.Label(self, text=label)
        self.label.pack(side="top", fill="both", expand=1)
        
        self.entryvar = Tkinter.StringVar(value=entrydef)
        self.entry = Tkinter.Entry(self, bg="yellow", width=width, textvariable=self.entryvar)
        self.entry.pack(side="top", fill="both", expand=1)
        
        self.entry.bind("<Button-1>", self.onclick)
        self.entry.bind("<FocusOut>", self.onleave)
    
    def onclick(self, event):
        try:
            float(event.widget.get())
        except:
            self.entryvar.set("")
        
    def onleave(self, event):
        try:
            float(event.widget.get())
            event.widget["bg"] = "white"
        except:
            self.entryvar.set(self.entrydef)
            event.widget["bg"] = "yellow"            
        
    def state(self):
        if self.entryvar.get() == self.entrydef:
            return None
        try:
            return float(self.entryvar.get())
        except:
            print "Error: Invalid Input"
            

            
class LabelCheckbutton(Tkinter.Frame):
    def __init__(self, parent, label, column, row, width=20):
        self.name = label
        Tkinter.Frame.__init__(self, parent)
        self.grid(column=column, row=row)
        
        self.buttonvar = Tkinter.IntVar()
        self.button = Tkinter.Checkbutton(self, text=label, width=width, variable=self.buttonvar)
        self.button.pack()
        
    def state(self):
        return self.buttonvar.get()