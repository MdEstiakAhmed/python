class People:
    """Base class for all type of people"""
    def __init__(self, id_number, name):
        self.id_number = id_number
        self.name = name

    def Id_number(self):
        print("id number: ", self.id_number)

    def Name(self):
        print("name: ", self.name)


class Teacher(People):
    """child class of People"""
    salary = 50000

    def salary_show(self):
        print(f"{self.name} salary is {self.salary}")


class Student(People):
    """child class of People"""
    cgpa = 3.9

    def cgpa_show(self):
        print(f"{self.name} cgpa is {self.cgpa}")


teacher1 = Teacher("14-45522-1", "XYZ")
teacher1.Id_number()
teacher1.Name()
teacher1.salary_show()

print()

student1 = Student("17-33434-1", "ABC")
student1.Id_number()
student1.Name()
student1.cgpa_show()

