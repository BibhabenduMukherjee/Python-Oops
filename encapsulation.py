# protected variable and private variable in pytho
# _variavble is a protected variable and __variable is a private variable
class Payman():
    def __init__(self , price):
        self.__final_price = price
    def get_value(self):
        return self.__final_price

book = Payman(100)
#book.__final_price = 0  # it is not a correct way everyone can access and make it's value in it's own for that we need encapsulation
#print(book.get_value())
book.__final_price = 1223312
print(book.__final_price)

################################################################ One more example ############

class XYZ12():
    def __init__(self, secret : str):
        self.secret = secret
    def __printSecret(self):
        print("Hello i am printing from XYZ12 Private method")
    def helper(self):
        print("I am a Helper function called the Private function")
        self.__printSecret()
    def NormalFun(self , name : str):
        self.name = name
        print("name is {} and secret is {}".format(name, self.secret))


ob1 = XYZ12("hfh736g3g383gf8")
# ob1.__printSecret()
ob1.NormalFun("your name")
#ob1.helper()