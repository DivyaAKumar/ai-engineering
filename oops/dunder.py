class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
student = Student("Div")

print(student)


#len
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Div", "Nav", "Harsh"])

print(len(team))

#combo
class Student:

    school = "ABC School"             # class variable

    def __init__(self, name, age):    # dunder method
        self.name = name              # instance variable
        self.age = age

    def introduce(self):              # instance method
        return f"{self.name}, {self.age}"

    def __str__(self):                # dunder method
        return self.name

student = Student("Div", 20)
student.name

student.school 

student.introduce()

print(student)


class Car:
    wheels = 4  # class variable
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

car1 = Car("Toyota", "Corolla", 2022)
car2= Car("Honda", "Civic", 2023)

car1.display_info() 
car2.display_info() 
print(car1)


