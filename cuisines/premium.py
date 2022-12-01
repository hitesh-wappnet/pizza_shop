class Premium(Cuisine):
    def __init__(self):
        super().__init__()
        self.setPrice()
        
    def setPrice(self):
        self.Reg = 165
        self.Med = 240
        self.Large = 395
