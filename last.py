
class Person:
    def __init__(self, surname, name, lastname, birth, sex):
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.birth = birth
        self.sex = sex

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect surname")
        self.__surname = s

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect name")
        self.__name = s

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect lastname")
        self.__lastname = s

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect birth")
        self.__birth = s

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect sex")
        self.__sex = s




class Sluzh(Person):

    def __init__(self, surname, name, lastname, birth, sex, orga, speciality, pos, salary, work_years):
        super().__init__(surname,name,lastname,birth,sex)
        self.orga = orga
        self.speciality = speciality
        self.pos= pos
        self.salary = salary
        self.work_years = work_years


    @property
    def orga(self):
        return self.__orga

    @orga.setter
    def orga(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect organization name")
        self.__orga = s

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect speciality")
        self.__speciality = s

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, s):
        if not isinstance(s, str) or not s :
            raise TypeError("Incorrect position")
        self.__pos = s

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        if not isinstance(s, int) or s < 0:
            raise TypeError("Incorrect salary")
        self.__salary = s

    @property
    def work_years(self):
        return self.__work_years

    @work_years.setter
    def work_years(self, s):
        if not isinstance(s, int) or s < 0 :
            raise TypeError("Incorrect organization name")
        self.__work_years = s

    def __str__(self):
        return f"{self.name} {self.surname} {self.lastname} {self.salary} {self.orga} {self.pos} {self.sex} {self.work_years}"

class Organization:
    def __init__(self, *args):
        self.workers = args

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, s):
        if not isinstance(s, object) or not s:
            raise TypeError("Incorrect data inputed")
        self.__workers = s

    def print(self):
        for x in self.workers:
            print(x.surname, x.name, x.lastname, x.birth, x.sex, x.orga, x.speciality, x.pos, x.salary, x.work_years)

    def search(self,num):
        for x in self.workers:
            if x.work_years >= num:
                num += 1
        return num-1

Maks=Sluzh("Vash","Maks","Serg","01.01.1992","W","Gogle","Engineer","Boss",1000,0)
Toha=Sluzh("Lolichka","Anechka","Serg","01.02.1993","W","Gogle","Engineer","GachiMan",1500,1)
Poa=Sluzh("Poa","Laer","Diego","08.01.1995","W","Gogle","Programemr","Boss",1000,2)
Gogle=Organization(Maks,Toha,Poa)

print(Maks)
