class Red_Indian(Premium):        
    def setIngredients(self):
        self.ingredients.append("Cheese")
        self.ingredients.append("Paneer")
        self.ingredients.append("Chilly")
        
    def __init__(self):
        super().__init__(self)
        self.setIngredients()
