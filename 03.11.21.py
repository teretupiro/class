class Person:
    def __init__(self,name,surname,gender='Male'):
        self.name=name
        self.surname=surname
        self.gender=gender







    def __str__(self):
        if self.gender=='Male':
         return f'Гражданин {self.surname+" "+self.name}'
        if self.gender=='Female':
          return  f'Гражданка {self.surname + " " + self.name}'

        elif self.gender!='Male'or'Female':
            self.gender = 'Male'
            print( 'Пусть будет мальчик ')
            return f'Гражданин {self.surname + " " + self.name}'




p1=Person('CHUCK','Norris')
print(p1)
p2=Person('Mila','Asia','Female')
print(p2)
p3=Person('David','Abas',True)
print(p3)
