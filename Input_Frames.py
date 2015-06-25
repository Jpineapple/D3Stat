#Frames
import Tkinter
from abc import ABCMeta, abstractmethod
from compound_widgets import *

class FrameShell(Tkinter.Frame, object):    
    __metaclass__ = ABCMeta
    name = None
    
    def __init__(self, parent, init_data):
        Tkinter.Frame.__init__(self, parent)
        self.frame_state = {}
        self.initialize_frame(parent, init_data)
    
    @abstractmethod
    def initialize_frame(self, parent, init_data):
        pass
        
    def get_state(self):
        for i, k in enumerate(self.winfo_children()):
            try:
                self.frame_state[k.name] = k.state()
            except:
                print "ERROR: Value for " + k.name + " invalid."
        
        return self.frame_state

    def set_state(self, dict):
        dict[self.name]
        
class DamageFrame(FrameShell):
    name = "Damage"
    
    def initialize_frame(self, parent, init_data):
        for i, k in enumerate(init_data):
            label, col, row = k
            LabelEntry(self, label, col, row, width=len(label)+5)


class StatsFrame(FrameShell):
    name = "Stats"
    
    def initialize_frame(self, parent, init_data):
        for i, k in enumerate(init_data):
            label, col, row = k
            LabelEntry(self, label, col, row, width=len(label)+5)

class CheckbuttonFrame(FrameShell):
    name = "Checkbutton"
    
    def initialize_frame(self, parent, init_data):
        for i, k in enumerate(init_data):
            label, col, row = k
            LabelCheckbutton(self, label, col, row, width=len(label)+5)