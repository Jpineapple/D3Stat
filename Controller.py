from ConfigRead import *

class Controller(object):       
    """ Contains methods that turn the associated config and save files
        into information used to generate the view.
    """
    def __init__(self):
        self.statsconfig = ConfigRead("ViewConfig.txt").parse()
        
    def get_config(self, keyword):
        """ Set up configuration for the frame denoted by keyword.
            Turn the data into a list of tuples containing 
            (label, column, row)
        """
        items = self.statsconfig[keyword]

        labelentry_data = []
        for i, k in enumerate(items):
            sep = k.split(", ")
            label, col, row = sep
            labelentry_data.append((label, int(col), int(row)))
        
        return labelentry_data
    
    