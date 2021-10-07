class People:

    def __init__(self, name,age,weight,height):
        self.name = name
        self.age=age
        self.weight=weight
        self.height=height




class Stutent(People):
    def study(self):

        print('i can study')


class Adult(People):

    def work(self):
        print('i can work')


dude1=Adult('JUAN',42,85,185)
print(dude1.name)
print(dude1.age)
print(dude1.weight)
print(dude1.height)
dude2=Adult('Pedro',56,77,192)
print(dude2.name)
print(dude2.age)
print(dude2.weight)
print(dude2.height)
dude3=Adult('Pablo',82,90,177)
print(dude3.name)
print(dude3.age)
print(dude3.weight)
print(dude3.height)
dude4=Adult('Carlos',33,80,200)
print(dude4.name)
print(dude4.age)
print(dude4.weight)
print(dude4.height)



student1=Stutent('Andrey',22,67,198)
print(student1.name)
print(student1.age)
print(student1.weight)
print(student1.height)
student2=Stutent('Peter',21,69,176)
print(student2.name)
print(student2.age)
print(student2.weight)
print(student2.height)
student3=Stutent('Nicolay',18,90,187)
print(student3.name)
print(student3.age)
print(student3.weight)
print(student3.height)
student4=Stutent('Igor',25,79,155)
print(student4.name)
print(student4.age)
print(student4.weight)
print(student4.height)








