class Person:
    def __init__(self,name,surname,gender='Male'):
        self.name=name
        self.surname=surname
        self.gender=gender
        if self.gender != 'Male'and self.gender!='Female':
            self.gender='Male'
            print('Я не распознал пол.Пусть это будет мальчик  ')
    def __str__(self):
        if self.gender=='Male':
         return f'Гражданин {self.surname+" "+self.name}'
        if self.gender=='Female':
          return  f'Гражданка {self.surname + " " + self.name}'
p1=Person('CHUCK','Norris')
print(p1)
p2=Person('Asia','Dalis','Female')
print(p2)
p3=Person('David','Abas','dddd')
print(p3)
