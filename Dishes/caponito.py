class Caponito(Classic):
    def setIngredients(self):
        self.ingredients.append("Capsicum")
        self.ingredients.append("Onion")
        self.ingredients.append("Tomato & Cheese")
        
    def __init__(self):
        super().__init__(self)
        self.setIngredients()
