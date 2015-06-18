class Model(object):
    def __init__(self):
        pass
    
    def get_mult(self, entrydict):
        self.multipliers = {}
        
        self.multipliers["Attribute"] = 1 + entrydict["Attribute"]/100
        
        self.multipliers["Crit"] = (1 + (entrydict["Crit Chance"]/100)
                                   *(entrydict["Crit Damage"])/100)
                                   
        self.multipliers["Element"] = (1+entrydict["Ele Dmg: Fire"]/100,
                                       1+entrydict["Ele Dmg: Cold"]/100,
                                       1+entrydict["Ele Dmg: Lightning"]/100,
                                       1+entrydict["Ele Dmg: Physical"]/100,
                                       1+entrydict["Ele Dmg: Arcane"]/100,
                                       1+entrydict["Ele Dmg: Holy"]/100,
                                       1+entrydict["Ele Dmg: Poison"]/100)
                                       
        self.multipliers["Elite"] = 1 + entrydict["Elite Dmg"]/100 
        
        if entrydict["Focus"] and entrydict["Restraint"]:
            self.multipliers["F&R"] = 1.5*1.5
            
        if entrydict["Cull"]:
            self.multipliers["Cull"] = 1.2
            
        self.multipliers["Gem 1"] = 1 + entrydict["Gem 1"]/100
        self.multipliers["Gem 2"] = 1 + entrydict["Gem 2"]/100 
        self.multipliers["Gem 3"] = 1 + entrydict["Gem 3"]/100 
        
        self.multipliers["Additive"] = 1 + entrydict["Additive"]/100
        
        self.multipliers["UH"] = (1 + 0.15*entrydict["UH"])*1.2
        
        return self.multipliers
            
    def damage(self, dmg_range, skill_mult, ele, multi, elite=False):
        self.ele_ref = {'Fire': 0, 'Cold': 1, 'Lightning': 2, 'Physical': 3,
                        'Arcane': 4, 'Holy': 5, 'Poison': 6}
        
        multi["Element"] = multi["Element"][self.ele_ref[ele]]
        if not elite:
            del multi["Elite"]
                
        self.val = multi.values()
               
        self.multiply = reduce(lambda x, y: x*y, self.val)
        for i, k in enumerate(dmg_range):
            dmg_range[i] = k * skill_mult * self.multiply

        return dmg_range

        
entrydict = {'Attribute': 9376.0, 'Elite Dmg': 15.0, 'Crit Damage': 505.0, 
             'Ele Dmg: Poison': 0.0, 'Ele Dmg: Holy': 0.0, 
             'Ele Dmg: Arcane': 0.0, 'Ele Dmg: Cold': 0.0, 
             'Ele Dmg: Lightning': 0.0, 'Crit Chance': 60.3,
             'Ele Dmg: Fire': 39.0, 'Ele Dmg: Physical': 15.0, "Focus": True,
             'Restraint': True, 'Cull': True, 'Gem 1': 25.2, 'Gem 2': 28.5,
             'Gem 3': 0.0, 'Additive': 20.0, 'UH': 78.0}

             test = Model()
yolo = test.get_mult(entrydict)
print yolo
holo = test.damage([1834.0,2911], 360.0, "Fire", yolo)
print holo
