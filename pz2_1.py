# Task 1.
# Create a class that descibes a Product of online store. As a Product fields you can use a price, description and product' dimensions.
# Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
# Create a class that describes an Order.
# - the order must contain data about the customer who carried it out and products. Implement a method for calculating the total order value.
class Product :
    def __init__(self,price,description,dimensions):
        if (isinstance(price,int) or isinstance(price,float)) and price>=0:
            self.price=price
        else:
            raise ValueError("incorrect price")
        self.description=description
        self.dimensions=dimensions


class Customer:
    def __init__(self,name,surname,telephone):
        if len(name)>2 and isinstance(name,str):
            self.name=name
        else:
            raise Exception("Pls norm name pls")
        if len(surname)>3 and isinstance(surname,str) :
            self.surname=surname
        else:
            raise Exception("Pls norm surname pls")
        self.surname=surname
        if len(telephone)>13 or len(telephone)<10 :
            raise Exception("incorrect telephone number")
        self.telephone=telephone


class order(object):
    def __init__(self,customer,*args):
        self.customer=customer
        self.args=args
    def sum(self):
        num = 0
        for x in self.args:
            num+=x.price
        return num
    def products_info(self):
        for x in self.args:
            print(x.price,x.description,x.dimensions)
    def customer_info(self):
            return (self.customer.name,self.customer.surname,self.customer.telephone)

Slava=Customer("Slavik","Moskal","+380965194692")
prod1=Product(211,"Chair","300x200x100")
prod2=Product(1000,"table","500x250x100")
prod3=Product(1020,"table","500x250x100")
ord=order(Slava,prod1,prod2,prod3)
print(ord.sum())
ord.products_info()
print(ord.customer_info())