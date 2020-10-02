class Nike():
    def __init__(self, joggers, sweaters, shirts, shoes, socks):
        self.joggers = joggers
        self.sweaters = sweaters
        self.shirts = shirts
        self.shoes = shoes 
        self.socks = socks
        self.cart = f"{self.joggers} joggers, {self.sweaters} sweaters, {self.shirts} shirts, {self.shoes} shoes and {self.socks} socks"
        
    @classmethod
    def the_90s_twist (cls):
        return cls(3, 5, 10, 4, 15)


Isaac = Nike.the_90s_twist()
print(type(Isaac))