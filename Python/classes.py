class Person:
  name = "hardik"
  city = "Indore"

p1=Person()
# del p1
print(p1.name)
print(p1.city)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
s1=Student('hardik',21)
s1.add_grade(85)
s1.add_grade(75)
s1.add_grade(95)
print(s1.name)
print(s1.age)
print(s1.grades)
print(s1.average_grade())
    

# Polymorphism in Action
# def describe(animal):
#     animal.make_sound()

# # Usage
# dog = Dog("Woof")
# cat = Cat("Whiskers")

# describe(dog)  # Output: Woof!
# describe(cat)  # Output: Meow!