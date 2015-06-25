class ConfigRead(object):
    """ Define methods for working with the D3Stat config files 
    [] denote section headings, # denotes a comment line
    ; are required on their own line to denote the end of a section
    """ 
    def __init__(self, file):
        self.file = open(file).readlines()

    def get_headings(self):
        """ Return a list of tuples with section (line number, headings)"""
        section_names = []
        # Search through the file and find the lines with a section heading
        for i, k in enumerate(self.file):
            if self.file[i].startswith("#"):    #ignore #(commented) lines
                continue
            elif (self.file[i].startswith("[") and
                  self.file[i].endswith("]\n")):
                name = k.strip()
                # Append the section line number and heading 
                section_names.append((i, name[1:-1]))
                
        return section_names
        
    def get_settings(self):
        """ Return a list. Each item is another list containing all the lines 
        under a section heading.
        """
        sections = self.get_headings()
        settings = []
        for i in sections:
            settings.append([])
        
        # for each section (line number, heading) tuple, 
        for i, indsec in enumerate(sections):
            ind, sec = indsec
            # navigate to one under the line number
            body = self.file[ind+1:]
            #store every line until it reaches the ';'
            for line in body:
                if line.startswith("#"):    #ignore #(commented) lines
                    continue
                elif (line).startswith(";"):
                    break
                else:
                    settings[i].append(line.strip())
                    
        return settings

    def parse(self):
        """ Returns a dictionary of headings(keys) and a list of 
        associated settings(values)
        """
        sections = self.get_headings()
        settings = self.get_settings()
        parsed = {}
        # for each heading, assign the heading name as a key 
        # and the list of settings as the value
        for i, indsec in enumerate(sections):
            ind, sec = indsec
            parsed[sec] = settings[i]
        
        return parsed


