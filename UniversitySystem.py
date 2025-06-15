class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Gender:{self.gender}\n\n")

class Lecturer(Person):
    def __init__(self, name, gender, employee_number, faculty):
        super().__init__(name, gender)
        self.employee_number = employee_number
        self.faculty = faculty

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Gender:{self.gender}")
        print(f"Employee Number:{self.employee_number}")
        print(f"Faculty:{self.faculty},\n\n")

class Student(Person):
    def __init__(self, name, gender, student_number, faculty):
        super().__init__(name, gender)
        self.student_number = student_number
        self.faculty = faculty
    
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Gender:{self.gender}")
        print(f"Student Number:{self.student_number}")
        print(f'Faculty:{self.faculty},\n\n')

class Staff(Person):
    def __init__(self, name, gender, staff_number):
        super().__init__(name, gender)
        self.staff_number = staff_number

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Gender:{self.gender}")
        print(f"Staff Number:{self.staff_number}")
    


#calling the methods
student1 = Student("Rachael", "Female", "STUOO1", "COCIS")
lecturer1 = Lecturer("Dr. Ruth", "Female", "LEC001", "COCIS")
staff1 = Staff("Mr. Johnson", "Male", "STAFF001,")

# Display their information
student1.display_info()
lecturer1.display_info()
staff1.display_info()
