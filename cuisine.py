class Cuisine:
    def __init__(self):
        self.Reg = None
        self.Med = None
        self.Large = None
        self.ingredients = []
        
    def setPrice(self):
        pass
    
    def setIngredients(self):
        pass
    
    def getIngredients(self):
        ret = ""
        for i in range(len(self.ingredients)):
            if i == len(self.ingredients)-1:
                ret = ret + "and " + self.ingredients[i]
            else:
                ret = ret + self.ingredients[i] + ", "
        return ret
    def getPrice(self,size):
        if size == "Reg":
            return self.Reg
        elif size == "Med":
            return self.Med
        elif size == "Large":
            return self.Large
        else:
            return "Invalid Choice !!"
