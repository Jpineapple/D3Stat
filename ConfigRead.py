class ConfigRead(object):
    def __init__(self, file):
        self.file = open(file).readlines()

    def get_headings(self):
        section_names = []
        for i, k in enumerate(self.file):
            if self.file[i].startswith("#"): 
                continue
            elif (self.file[i].startswith("[") and
                  self.file[i].endswith("]\n")):
                name = k.strip()
                section_names.append((i, name[1:-1]))
                
        return section_names
        
    def get_settings(self):
        sections = self.get_headings()
        settings = []
        for i in sections:
            settings.append([])
        
        for i, indsec in enumerate(sections):
            ind, sec = indsec
            body = self.file[ind+1:]
            for line in body:
                if line.startswith("#"):
                    continue
                elif (line).startswith(";"):
                    break
                else:
                    settings[i].append(line.strip())
                    
        return settings

    def parse(self):
        sections = self.get_headings()
        settings = self.get_settings()
        parsed = {}
        for i, indsec in enumerate(sections):
            ind, sec = indsec
            parsed[sec] = settings[i]
        
        return parsed


