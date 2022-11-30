class Premium(Cuisine):
    def setPrice(self):
        self.Reg = 165
        self.Med = 240
        self.Large = 395
        
    def __init__(self):
        super().__init__(self)
        self.setPrice()
