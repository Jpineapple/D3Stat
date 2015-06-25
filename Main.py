import Tkinter
from tkFileDialog import askopenfilename
from Controller import *
from Input_Frames import *

class Win(Tkinter.Tk, object):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.control = Controller()
        self.initialize_frames()
        self.menu_setup()
        
    def initialize_frames(self):       
        #Import the configuration for the damage frame and generate it
        damage_configdata = self.control.get_config("Damage")
        self.damage_frame = DamageFrame(self, damage_configdata)
        self.damage_frame.grid(column=0, row=0, padx=5, pady=5)
        
        #Import the configuration for the statistics frame and generate it
        statistics_configdata = self.control.get_config("Statistics")
        self.statistics_frame = StatsFrame(self, statistics_configdata)
        self.statistics_frame.grid(column=0, row=1, sticky="nw", padx=5, pady=5)
        
        #Import the configuration for 
        checkbutton_configdata = self.control.get_config("Checkbutton")
        self.checkbutton_frame = CheckbuttonFrame(self, checkbutton_configdata)
        self.checkbutton_frame.grid(column=1, row=0, rowspan=2, sticky="n", padx=5, pady=5)
        
        test = self.winfo_children()
        self.frame_store = {}
        for child in test:
            self.frame_store[child.name] = child
            
    def menu_setup(self):
        self.menubar = Tkinter.Menu(self)
        self.menubar.add_command(label="Open", command=self.get_file)
        self.menubar.add_command(label="Save", command=self.save_file)
        
        self.config(menu=self.menubar)
        
    def get_file(self):
        self.filename = askopenfilename()
        savdict = self.control.open_sav(self.filename)
        for key in self.frame_store.keys(): 
            input = savdict[key]
            for entry in self.frame_store[key].winfo_children():
                try:
                    entry.entry.focus_set()
                    entry.entryvar.set(input[entry.label.cget("text")])
                except:
                    continue
        self.focus_set()
        
    def save_file(self):
        self.focus_set()
        open("D3Save.txt", "w").truncate()
        for key in self.frame_store.keys():
            name = key
            frame = self.frame_store[key]
            
            update = frame.get_state()
            sav = str(update)[1:-1]
            with open("D3Save.txt", "a") as f:
                f.write("[" + name + "]" + "\n")
                for line in sav.split(", "):
                    f.write(line + "\n")
                f.write(";\n")

if __name__ == "__main__":
    app = Win(None)
    app.title("Diablo?!?")
    app.mainloop()