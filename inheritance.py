# base class 

class Base:
    def __init__(self , name : str , price : float):
        self.name = name
        self.price = price

        def a1(self):
            print("Calling from Base class")

# Although it has not name and price attributes it's showing correct
# output because this class inherits all attributs from Base class
class Children1(Base):
    def __init__(self , name : str , price : float):
        Base.__init__(self , name , price)

class Children2(Base):
    pass


s = Children1("Realme Phone" , 21000)

print(s.name)