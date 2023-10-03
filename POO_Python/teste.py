class Person:
    def __init__(self, name, age, gender, active):
        self.name = name
        self.age = age
        self.gender = gender


    def desable(self):
        self.active = False
        print(f'{person1} has been deactivated.')
        
person1 = Person('Eduardo', 27, 'M', True)
person1.desable()
person1.active = True
print(person1.active)

