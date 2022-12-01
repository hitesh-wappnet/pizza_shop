class Classic(Cuisine):
    def __init__(self):
        super().__init__()
        self.setPrice()
        
    def setPrice(self):
        self.Reg = 135
        self.Med = 210
        self.Large = 360
