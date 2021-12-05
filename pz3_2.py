# Pizzeria offers pizza-of-the-day for business lunch.
# The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.

from datetime import datetime as date
import json


extra_ingredient = 15
database = "pizzeria.json"

class pizza:
    def __init__(self,type,*ingredients):
        self.type = type
        with open(database, 'r') as f:
            pizza_data = json.load(f)["pizzaoftheday"][type]
        self.price = pizza_data["price"]
        self.ingredients = pizza_data["ingredients"]
        if ingredients:
            for additional in ingredients:
                self.price += extra_ingredient
                self.ingredients[additional]=1

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self,t):
        if not isinstance(t,str) or not t:
            raise TypeError("Input correct pizza")
        self.__type = t

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,p):
        if isinstance(p,int ) or isinstance(p,float) and p>0:
            self.__price = p
        else:
            raise TypeError("Incorrect price")

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self,t):
        if not isinstance(t,dict) or not t:
            raise TypeError("Input correct ingredient")
        self.__ingredients = t

class pizza_of_the_day(pizza):
    def __init__(self,*ingredients):
        day = date.today().strftime("%A")
        match day:
            case "Monday":
                type = "54 cheese"
            case "Tuesday":
                type = "pepperoni"
            case "Wednesday":
                type = "margorita"
            case "Thursday":
                type = "hawaiian"
            case "Friday":
                type = "buffalo"
            case "Saturday":
                type = "bbq_chicken"
            case "Sunday":
                type = "veggie"
        super().__init__(type,*ingredients)
        with open(database, 'r') as f:
            pizza_data = json.load(f)["pizzaoftheday"][type]
        self.price = int(pizza_data["price"])*0.5
        for x in ingredients:
            self.price+=extra_ingredient

class order:
    def __init__(self,name, *args):
        self.name = name
        self.pizza=args


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,n):
        if not isinstance(n,str) or not n:
            raise TypeError("Incorect name")
        self.__name=n

    def show_order_short(self):
        p=0
        print("Customer name: "+self.name)
        for x in self.pizza:
            print(x.type+"    ",x.price)
            p += x.price
        print("Overal: ",p)

    def show_order(self):
        p=0
        print("Customer name: "+self.name)
        for x in self.pizza:
            print(x.type+" ingredients: ",x.ingredients)
            p += x.price
        print("Overal: ", p)


Maks=pizza("54 cheese","tomato","mushrooms","meat")
day=pizza_of_the_day("mushrooms")
zakaz=order("Slavik Marlow",day,Maks)
zakaz.show_order_short()