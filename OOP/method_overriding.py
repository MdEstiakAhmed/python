class People:
    """Base class for all type of people"""
    def __init__(self, id_number, name):
        self.id_number = id_number
        self.name = name

    def details(self):
        print(f"name: {self.name}")
        print(f"id: {self.id_number}")


class Teacher(People):
    """child class of People"""
    def __init__(self, id_number, name, salary):
        super().__init__(id_number, name)
        self.salary = salary

    def details(self):
        super().details()
        print(f"salary: {self.salary}")


class Student(People):
    """child class of People"""
    def __init__(self, id_number, name, cgpa):
        super().__init__(id_number, name)
        self.cgpa = cgpa

    def details(self):
        super().details()
        print(f"cgpa: {self.cgpa}")


teacher1 = Teacher("14-45522-1", "XYZ", 40000)
teacher1.details()

print()

student1 = Student("17-33434-1", "ABC", 3.8)
student1.details()
