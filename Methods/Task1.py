from datetime import date

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def ptintname(self):
        print(self.name, self.age)

    @classmethod
    def classmethod(cls, year):
        return Person("Anna", date.today().year - year)

    @staticmethod
    def staticmethod(age):
        if age < 18:
            return "no"
        else:
            return "yes"


anna = (Person.classmethod(2004))
print(anna.name)
print(anna.age)
print(anna.staticmethod(18))