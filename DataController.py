from ConfigRead import *

class DataController(object):       
    def gui_data(self):
        conf = ConfigRead("DataConfig.txt")
        raw_data = conf.parse()
        gdata = raw_data["Label Entries"]
        
        self.labelentry_data = []
        
        for i, k in enumerate(gdata):
            sep = gdata[i].split(", ")
            label, col, row = sep
            self.labelentry_data.append((label, int(col), int(row)))
        
        return self.labelentry_data

test = DataController()

print test.gui_data()