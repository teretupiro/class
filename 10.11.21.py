class Person:
    def __init__(self, name):
        self.__name = name  
        self.__age = 1  

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


p1 = Person("Alex")
p1.display_info()
print(tom.age)
p1.age = -486
p1.age = 36


p1.display_info()
