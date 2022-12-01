class Supreme(Cuisine):
    def __init__(self):
        super().__init__()
        self.setPrice()
        
    def setPrice(self):
        self.Reg = 190
        self.Med = 290
        self.Large = 425
