#Task 3.
#The class GROUP contains a sequence of instances of the class STUDENT.
#The class STUDENT contains the student's name, surname, record book number and grades.
#Determine the required attributes-data and attributes-methods in classes GROUP and STUDENT.
#'Find the average score of each student. Output to the standard output stream the five students with the highest average score.
#Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.
class student:
    def __init__(self,name,surname,math,eng,pe):
        self.name=name
        self.surname=surname
        self.math=math
        self.eng =eng
        self.pe = pe

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,s):
        if not isinstance(s,str) or len(s)<3:
            raise TypeError("Normal name pls")
        self.__name=s

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self,s):
        if not isinstance(s,str) or len(s)<3:
            raise TypeError("Normal surname pls")
        self.__surname=s

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self,val):
        if not isinstance(val,int) or val<1 or val>12:
            raise TypeError("Input correct grade")
        self.__math=val

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self,val):
        if not isinstance(val,int) or val<1 or val>12:
            raise TypeError("Input correct grade")
        self.__eng=val

    @property
    def pe(self):
        return self.__pe

    @pe.setter
    def pe(self,val):
        if not isinstance(val,int) or val<1 or val>12:
            raise TypeError("Input correct grade")
        self.__pe=val

class group(object):
    def __init__(self,name, *args):
        self.name = name
        self.students=sorted(args, key=lambda student: student.surname, reverse=False)

    def show(self):
        print(" Surame      Name      Math Eng Pe")
        for x in self.students:
            print("{0:10}".format(x.surname)+"{0:13}".format(x.name)+"{0:3} ".format(x.math)+"{0:3} ".format(x.eng)+"{0:3} ".format(x.pe))

    def best_stud(self):
        print(" Surname      Name      Aver")
        for x in sorted(self.students, key=lambda student: student.math, reverse=True):
            print("{0:10}".format(x.surname)+"{0:13}".format(x.name)+"{0:3} ".format(round(((x.math+x.pe+x.eng)/3),2)))

toha=student("Anechka","Lolichka",11,10,10)
whatislove=student("Reaper","King",1,1,1)
maks=student("Pudge","Meat",1,10,12)
Abdul=student("Abdul","AKart",4,12,7)
Kolya=student("Kolya","Sever",12,12,12)#dont hurt me pls
slava=student("Slavik","Moskal",6,9,3)
zheka=student("Zheka","Napass",7,7,4)
zahar=student("Zahar","Anime",7,9,9)
ab21=group("ab21",toha,whatislove,maks,Abdul,Kolya,slava,zheka,zahar)
print(ab21.best_stud())
print(ab21.show())