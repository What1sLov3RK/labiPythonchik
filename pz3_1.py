

#tickets for Face concert

import uuid
class Ticket:
    def __init__(self):
        self.price = 300
        self.id = uuid.uuid1()
        self.type = "regular"
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        if not isinstance(p,int) or p<0 or p>3000:
            raise TypeError("Incorrect price")
        self.__price = p

    def getticket(self):
        return("Ticket type : "+self.type+'\n'+"Ticket price: "+str(self.price)+"\n"+"Ticked id : "+str(self.id))

class Student(Ticket):
    def __init__(self):
        Ticket.__init__(self)
        self.price = int(self.price*0.5)
        self.type = "Student"

class Advance(Ticket):
    def __init__(self):
        Ticket.__init__(self)
        self.price=int(self.price*0.6)
        self.type = "Advance"

class Late(Ticket):
    def __init__(self):
        Ticket.__init__(self)
        self.price=int(self.price*1.1)
        self.type = "Late"

test=Ticket()
WhatIsLove=Student()
Antony=Advance()
Maksik=Late()
print(test.getticket())
print(WhatIsLove.getticket())
print(Antony.getticket())
print(Maksik.getticket())