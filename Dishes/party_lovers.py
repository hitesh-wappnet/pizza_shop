class Party_Lovers(Premium):
    def setIngredients(self):
        self.ingredients.append("Cheese")
        self.ingredients.append("Sweer Corn")
        self.ingredients.append("Capsicum")
        self.ingredients.append("Tomato")
        
    def __init__(self):
        super().__init__()
        self.setIngredients()
