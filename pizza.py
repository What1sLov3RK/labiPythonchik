# Pizzeria offers pizza-of-the-day for business lunch.
# The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers.
# They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day.
# Write a program that will form orders from customers.

from datetime import datetime
import json

EXTRA_INGREDIENT_PRICE = 10
STORAGE_DATABASE_FILE = "storage.json"
PIZZERIA_DATABASE_FILE = "pizzeria.json"

class NoIngredientsError(Exception):
	def __init__(self, message) -> None:
		self.message = message


class WrongAdditionalIngredientError(Exception):
	def __init__(self, message) -> None:
		self.message = message

class Pizza_of_the_day:
	def __init__(self, date, *additional_ingredients) -> None:
			with open(PIZZERIA_DATABASE_FILE, 'r') as f:
				pizza_data = json.load(f)["pizzaoftheday"][date]
			self.type =  pizza_data["type"]
			self.price = pizza_data["price"]
			self.ingredients = pizza_data["ingredients"]
			for ingr in additional_ingredients:
				if not ingr in self.__ingredients:
					raise WrongAdditionalIngredientError(f"{ingr} is not allowed to be in this pizza")
				self.price+=EXTRA_INGREDIENT_PRICE
				self.__ingredients[ingr] += 1

	def __str__ (self):
		return f'Type: {self.type} \nPrice: {self.price} \nIngredients: {", ".join(map(str, self.ingredients))}'
				
	@property
	def type(self):
		return self.__type

	@type.setter
	def type(self, value):
		if not value:
			raise ValueError("Empty string")
		if not isinstance(value, str):
			raise TypeError
		self.__type = value

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value):
		if not value > 0:
			raise ValueError("Price must be greater than zero")
		if not isinstance(value, int):
			raise TypeError
		self.__price = value

	@property
	def ingredients(self):
		return self.__ingredients

	@ingredients.setter
	def ingredients(self, value):
		if not isinstance(value, dict):
			raise TypeError
		self.__ingredients = value
		

class MondayPizza(Pizza_of_the_day):
    def __init__(self, date, *additional_ingredients):
        super().__init__(date, *additional_ingredients)
	
class TuesdayPizza(Pizza_of_the_day):
    def __init__(self, date, *additional_ingredients):
        super().__init__(date, *additional_ingredients)


class WednesdayPizza(Pizza_of_the_day):
    def __init__(self, date, *additional_ingredients):
        super().__init__(date, *additional_ingredients)


class ThursdayPizza(Pizza_of_the_day):
    def __init__(self, date, *additional_ingredients):
        super().__init__(date, *additional_ingredients)


class FridayPizza(Pizza_of_the_day):
    def __init__(self, date, *additional_ingredients):
        super().__init__(date, *additional_ingredients)


class SaturdayPizza(Pizza_of_the_day):
    def __init__(self, date, *additional_ingredients):
        super().__init__(date, *additional_ingredients)


class SundayPizza(Pizza_of_the_day):
    def __init__(self, date, *additional_ingredients):
        super().__init__(date, *additional_ingredients)


class Storage:
	storage_database: str = STORAGE_DATABASE_FILE

	@classmethod
	def storage_check(cls, pizza: Pizza_of_the_day):
		with open(cls.storage_database, 'r') as f:
			data = json.load(f)["ingredients"]
		for ingr, amount in pizza.ingredients.items():
			if data[ingr] - amount < 0:
				return False
		return True

	@classmethod
	def update_storage(cls, pizza: Pizza_of_the_day):
		with open(cls.storage_database, 'r') as f:
			ingred = json.load(f)
		for pizza_ingr, amount in pizza.ingredients.items():
			ingred["ingredients"][pizza_ingr] -= amount
		with open(cls.storage_database, 'w') as f:
			json.dump(ingred, f, indent=4)



class Pizzeria:
	@staticmethod
	def cook_pizza(*additional_ingredients):
		date = datetime.today().strftime("%A").lower()
		match date:
			case "monday":
				pizza = MondayPizza(date, *additional_ingredients)
			case "tuesday":
				pizza = TuesdayPizza(date, *additional_ingredients)
			case "wednesday":
				pizza = WednesdayPizza(date, *additional_ingredients)
			case "thursday":
				pizza = ThursdayPizza(date, *additional_ingredients)
			case "friday":
				pizza = FridayPizza(date, *additional_ingredients)
			case "saturday":
				pizza = SaturdayPizza(date, *additional_ingredients)
			case "sunday":
				pizza = SundayPizza(date, *additional_ingredients)

		if not Storage.storage_check(pizza):
			raise NoIngredientsError("No ingredients left")
		Storage.update_storage(pizza)
		return pizza



class Order_Pizza_of_the_day:
	def __init__(self, *additional_ingredients) -> None:
		self.pizza =  Pizzeria.cook_pizza(*additional_ingredients)
		self.additional_ingredients = list(additional_ingredients)

	def __str__(self) -> str:
		return f'{self.pizza} \nAdditional ingredients: {", ".join(map(str, self.additional_ingredients))}'

	@property
	def pizza(self):
		return self.__pizza

	@pizza.setter
	def pizza(self, value):
		if not isinstance(value, Pizza_of_the_day):
			raise TypeError("Wrong type")
		self.__pizza = value

	@property
	def additional_ingredients(self):
		return self.__additional_ingredients

	@additional_ingredients.setter
	def additional_ingredients(self, value):
		if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
			raise TypeError("Wrong type")
		if not all(x for x in value):
			raise ValueError("Wrong value")
		self.__additional_ingredients = value



if __name__ == "__main__":
	print(Order_Pizza_of_the_day("mozzarella", "onion"))