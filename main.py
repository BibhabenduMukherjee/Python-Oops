
# create the class and write pass to do nothing 
class Item:
    pass


#create a object of that class 
item =  Item()

#adding some attributes to the object
item.name = "Phone"
item.price = 10000
item.quantity = 5

print(item.name) #Phone


################################

#adding any method to a class to do something

#create another  class just like above

class Item2:

    # for creating methods or functions use def keyword
    # WHY self -> at the time of calling any methods that method will expect 
    # the object itself as a first argument 
    def calculate_total_price(self , x , y):
        return x*y


item2 =  Item2()

item2.name = "Laptop"
item2.price = 35000
item2.quantity = 12

#calling the method 
result = item2.calculate_total_price(item2.price , item2.quantity)
print(result)



# above example is contains 3 attributes but if we have more attributes
# it is not efficiant to do item2.name , item.price ... so on so forth
# here we will going to use a special function in python called __init__
# __init__() [called constractor] function is called automatically when a object has been created

class Item3:
    def __init__(self, name , price , quantity , brand):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brand = brand
       
    def printAllDetails(self):
        print(self.name , self.price , self.quantity ,self.brand)
    def calculate_total_price1(self):
        return self.price * self.quantity 

# this time we pass our attributes as a arguments in the Item3
item3 = Item3("iphone 11 pro" , 120000, 2 , "apple")
item3.printAllDetails()

# you also add some attributes withOut using __init__() function
item3.wideAngleCameraView = True

# print the total price this time we don't pass price and quantitiy as a param'
# because now we have __init__ function that know the attributes
print(item3.calculate_total_price1())


##############-------------------------------------------------------#################

# NOW For extra checking of attributes datatype 
# create a class it's same as above class

class Item4:

    # constructor
    def __init__(self , name : str , price : float):
        pass

    # all is same just like the above here we see by using (name : str)
    # we strictly except only string datatype as a name 
    # and price as a float(float can be same as int)


#####------------------------------------------------------------------------------###
# now we try to validate our __init__ function using assert function

class Item5:
    def __init__(self , name: str , price: float , quantity):
        # Run the validations to the recieved arguments we cannot pass price or quantity as negative value
        assert price >= 0 , f"Price {price} and Quantity {quantity} is not greate than or equal to 0"
        assert quantity>=0 , f"Price {price} and Quantity {quantity} is not greate than or equal to 0"
        
        # Assign self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # format method is just like placeholder it places name , price and quantity in the -> {}
        # that pass as a agrument one after another
        print("The name of the phone is {} and the price of {} phone is {} ".format(self.name , self.price , self.quantity))


item5 = Item5("iphone 12 pro max" , 126000 , 1)

################################################################

# create a class attributes

class Item6:
    pay_rate = 0.7 # pay-rate is a class label attribute
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price           # {INSTANCE LAVEL}
        self.quantity = quantity
        # here pay_rate is not available 

     
    def apply_discount(self):
        self.price = self.price* Item6.pay_rate



item6= Item6("iphone SE" , 32000 , 1) # object created 
item6.apply_discount() # discount for Phone 
print(item6.price)

# now apply a discount for a laptop with
item6_laptop = Item6("Dell Xperon" ,67000 , 1)
item6_laptop.pay_rate = 0.4 # discount forpay_rate  = 0.4 # set from here that will not effect the other pay_rate for Phone
item6_laptop.apply_discount() 
print(item6_laptop.price)


# it's way to accessing the class attributes      
print(Item6.pay_rate)

# try a another way
print(item6.pay_rate)   ### WHY this work ###

## TRY TO UNDERSTAND
# the constructor has not any idea what is pay_rate it happens
# it searchs in instance level first it could not find anything
# then go to class label 


print(Item6.__dict__)  # this will give me all the attributes for class lavel
print(item6.__dict__)  # item6 is a instance of Item6 so it will given all the instance lavel attributes