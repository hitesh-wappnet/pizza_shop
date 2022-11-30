class Tomichi(Classic): 
    def setIngredients(self):
        self.ingredients.append("Tomato")
        self.ingredients.append("Onion")
        self.ingredients.append("Chilly & Cheese")
        
    def __init__(self):
        super().__init__(self)
        self.setIngredients()
