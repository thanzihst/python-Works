class Dishes:
    name:str

    price:int

    def __init__(self,name,price):
        self.name=name

        self.price=price


    def __str__(self):
        return self.name
    

dish1=Dishes()
    

class Resturant :

    name:str
    place:str
    dishess:[]

    def __init__(self,name,place):
        self.name=name
        self.place=place

        
