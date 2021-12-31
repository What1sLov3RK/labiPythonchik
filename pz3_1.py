# tickets for Face concert

import uuid


PRICE = 300
ADVANCE_TICKET_MULTIPLIER = 0.6
LATE_TICKET_MULTIPLIER = 1.1
STUDENT_TICKET_MULTIPLIER = 0.5


class Ticket:

    def __init__(self):
        self.price = PRICE
        self.id = uuid.uuid1()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        if not isinstance(p, int):
            raise TypeError("Incorrect price")
        if not p > 0:
            raise ValueError("Price cant be less than zero!")
        self.__price = p

    def __str__(self):
        return ("Ticket type : " + self.type + '\n' + "Ticket price: " + str(self.price) + "\n"
                + "Ticked id : " + str(self.id))


class Regular(Ticket):
    def __init__(self):
        super().__init__()
        self.price= self.price
        self.type= "Regular"




class Student(Ticket):
    def __init__(self):
        super().__init__()
        self.price = int(self.price * STUDENT_TICKET_MULTIPLIER)
        self.type = "Student"


class Advance(Ticket):
    def __init__(self):
        super().__init__()
        self.price = int(self.price * ADVANCE_TICKET_MULTIPLIER)
        self.type = "Advance"


class Late(Ticket):
    def __init__(self):
        super().__init__()
        self.price = int(self.price * LATE_TICKET_MULTIPLIER)
        self.type = "Late"


test = Regular()
WhatIsLove = Student()
Antony = Advance()
Maksik = Late()
print(test)
print(WhatIsLove)
print(Antony)
print(Maksik)
