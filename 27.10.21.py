class Dog:
    def __init__(self,name,age ):
        self.name=name
        self.age=age
    def description(self):
        return f'{self.name} is {self.age} years old'
    def speak(self,sound):
        return f"{self.name} says {sound}"
''

dog1=Dog('Mark',5)
print(dog1.description())
print(dog1.speak('WOOF'))
