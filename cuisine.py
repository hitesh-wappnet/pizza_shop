import os
from abc import ABC, abstractmethod

class Cuisine(ABC):
    def __init__(self):
        self.Reg = None
        self.Med = None
        self.Large = None
        self.ingredients = []
    
    @abstractmethod
    def setPrice(self):
        pass
    
    def setIngredients(self,ing):
        for i in ing:
            self.ingredients.append(i)
    
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
        else:
            return self.Large
