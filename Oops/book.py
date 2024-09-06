class Book:
    
    title:str

    author:str

    price:int

    language:str

    def __init__(self,title,author,price,lang) :#inicilzing instance varibale
        self.title=title

        self.author=author

        self.price=price

        self.language=lang

    def display_book(self):
        print(self.title,self.author,self.price,self.language)
    
    def __str__(self):
        return self.title




book1=Book("goatlife","benyamin",700,"malayalam")


book1.display_book()

print(book1)


