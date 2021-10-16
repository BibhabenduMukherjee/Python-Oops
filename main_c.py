#Here we will see how to create list of all objects 
import csv

class Item:
    all = []

    def __init__(self , name : str , price : float , quantity ):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self) # Item.all {accessing the class lavel attributes}
    # a good way to represents your all objects 
    def __repr__(self):
        return f"Item('{self.name}', {self.price} , {self.quantity})"
    

    # read our csv value
    # for that create a class lavel method 
    # cls is class object that must be passed as a first arguments
    @classmethod
    def instantiate_from_csv(cls):
        with open('elements.csv' , 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)



#item1 = Item("Lenovo Laptop" , 40000 , 1)
#item2 = Item("Macbook air" , 270000 , 3)
#item3 = Item("Ipad mini" , 450000 , 5)
#item = Item("Moto Phone" , 42000 , 6)

print(Item.all) # out put is just like '<__main__.Item object at 0x1006dcf10> 🎃'

# for instance in Item.all:
#     print(instance.name)

Item.instantiate_from_csv() #calling the class method