class Classic(Cuisine):        
    def setPrice(self):
        self.Reg = 135
        self.Med = 210
        self.Large = 360
        
    def __init__(self):
        super().__init__(self)
        self.setPrice()
