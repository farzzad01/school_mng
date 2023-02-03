#############################


class City:
    def __init__(self):
        


class School:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.classes = Classes
        
    def add_class(self, class_name, class_code):
        self.classes[class_code] = Classes(class_name, class_code)
        
    def get_class(self, class_code):
        return self.classes[class_code]
    
    def show_all_info(self):
        print("School Name: ", self.name)
        print("School Code: ", self.code)
        print("Classes: ")
        for class_code in self.classes:
            class_info = self.classes[class_code]
            print("Class Name: ", class_info.name)
            print("Class Code: ", class_info.code)
            print("Students: ")
            for student in class_info.students:
                print("Name: ", student.name)
                print("Birthdate: ", student.birthdate)
                print("ID: ", student.id)
                print("Major: ", student.major)
            print("   Teachers: ")
            for teacher in class_info.teachers:
                print("Name: ", teacher.name)
                print("ID: ", teacher.id)
                print("Birthdate: ", teacher.birthdate)
                print("Teacher Code: ", teacher.teacher_code)
                print("Hire Date: ", teacher.hire_date)

class School:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.classes = {}
        self.teachers = []
        
    def add_class(self, class_name, class_code):
        self.classes[class_code] = Class(class_name, class_code)
        
    def get_class(self, class_code):
        return self.classes[class_code]
    
    def add_teacher(self, name, id, birthdate, teacher_code, hire_date):
        self.teachers.append(Teacher(name, id, birthdate, teacher_code, hire_date, self))
        
    def show_all_info(self):
        print("School Name: ", self.name)
        print("School Code: ", self.code)
        print("Classes: ")
        for class_code in self.classes:
            class_info = self.classes[class_code]
            print("   Class Name: ", class_info.name)
            print("   Class Code: ", class_info.code)
            print("   Students: ")
            for student in class_info.students:
                print("      Name: ", student.name)
                print("      Birthdate: ", student.birthdate)
                print("      ID: ", student.id)
                print("      Major: ", student.major)
            print("   Teachers: ")
            for teacher in class_info.teachers:
                print("      Name: ", teacher.name)
                print("      ID: ", teacher.id)
                print("      Birthdate: ", teacher.birthdate)
                print("      Teacher Code: ", teacher.teacher_code)
                print("      Hire Date: ", teacher.hire_date)
                
    def show_teacher_info(self, teacher_code):
        for teacher in self.teachers:
            if teacher.teacher_code == teacher_code:
                print("Teacher Name: ", teacher.name)
                print("Teacher ID: ", teacher.id)
                print("Birthdate: ", teacher.birthdate)
                print("Teacher Code: ", teacher.teacher_code)
                print("Hire Date: ", teacher.hire_date)
                print("School: ", teacher.school.name)
                return
        print("Teacher with code", teacher_code, "not found.")






class Person:
    def __init__(self,fname,lname,birthdte,natcode):
        self.fname = fname
        self.lname = lname
        self.birthdte = birthdte
        self.natcode = natcode

    def read_person_info(self):
        self.fname = input('enter first name: ')
        self.lname = input('enter last name')
        self.birthdte = input('enter birth date')
        self.natcode = input('enter your national code')
    

    def show_full_name(self):
        print(f'first name is {self.fname}')
    def show_birthdate(self):
        print(f'birth date is {self.birthdte}')
    def show_natcode(self):
        print(f'nat code is {self.natcode}')


    def get_first_name(self):
        return self.fname 
    def get_last_name(self):
        return self.lname
    def get_birthdate(self):
        return self.birthdte
    def get_natcode(self):
        return self.natcode 

    def show_all_info(self):
        return f'name is {self.fname} {self.lname} birth date is s{self.birthdte} national code is {self.natcode}'

    def delete_person(self):
        del self.fname
        del self.lname
        del self.birthdte
        del self.natcode


class Student(Person):
    def __init__(self, fname, lname, birthdte, natcode, major):
        super().__init__(fname, lname, birthdte, natcode)
        self.major = major

    def read_student_major(self):
        self.major = input('enter major ')

    def show_student_major(self):
        print(f'major student is {self.major}')

    def get_student_major(self):
        return self.major

    def read_student_info(self):
        super().read_person_info
        self.read_student_major()

    def show_student_infom(self):
        super().show_full_name
        super().show_birthdate
        super().show_natcode
        self.show_student_major()


class Teacher(Person):
    def __init__(self, fname, lname, birthdte, natcode,teach_code,hite_tme):
        super().__init__(fname, lname, birthdte, natcode)
        self.teach_code = teach_code
        self.hite_tme = hite_tme
    
    def read_teach_code(self):
        self.teach_code = input('enter teacher code')
    
    def show_teach_code(self):
        print(f'teacher code is {self.teach_code}')
    
    def read_hire_time(self):
        self.hite_tme = input('enter hire time')

    def show_hire_time(self):
        print(f'hite time is {self.hite_tme}')

    def get_hire_time(self):
        return self.hite_tme
    
    def get_teach_code(self):
        return self.teach_code

    def get_full_name(self):
        return(f'name is {self.fname} {self.lname}')

    def read_teacher_inform(self):
        super().read_person_info
        self.read_teach_code
        self.read_hire_time

    def show_teacher_inform(self):
        super().show_all_info
        self.show_hire_time()
        self.show_teach_code()


class Classes:
    def __init__(self, class_name, class_code):
        self.class_name = class_name
        self.class_code = class_code
        self.students = []
        self.teacher = Teacher()
        
    def class_info(self):
        num_stu = input('enter number of students')
        self.students = num_stu

    def read_class_code(self):
        self.class_code = input('enter class name ')
    def show_class_code(self):
        print(f'class code is {self.class_code}')

    def read_class_name(self):
        self.class_name = input('enter class name')
    def show_class_name(self):
        print(f'class name is {self.class_name}')

    def get_class_code(self):
        return self.class_code
    def get_class_name(self):
        return self.class_name

    def add_student(self, name, birthdate, id, major):
        self.students.append(Student(name, birthdate, id, major))
        

    def get_teacher_natcode(self):
        return Teacher.get_natcode()

    def show_teacher_name(self):
        return Teacher.get_full_name


    def read_class_info(self):
        self.read_class_code()
        self.read_class_name()
        Teacher.read_teacher_inform()
        for i in range(self.students + 1):
            Student[i].read_student_info()

    def show_class_info(self):
        self.show_class_code
        self.show_class_info
        Teacher.show_teacher_inform()
        for i in range(self.students + 1):
            print(Student[i].show_student_infom)

    def find_stu_by_fullname(self,fname,lname):
        find = False
        for i in range(Student + 1):
            if fname == Student[i].get_first_name():
                if lname == Student[i].get_last_name():
                    print(f'student : {Student[i]} founded ')
                    Student[i].show_full_name()
                    find = True
        return find
    
    def show_teacher_of_class(self):
        Teacher.show_full_name


class Class:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []
        self.teachers = []
        
    def add_student(self, name, birthdate, id, major):
        self.students.append(Student(name, birthdate, id, major))
        
    def add_teacher(self, name, id, birthdate, teacher_code, hire_date):
        self.teachers.append(Teacher(name, id, birthdate, teacher_code, hire_date))

class Student:
    def __init__(self, name, birthdate, id, major):
        self.name = name
        self.birthdate = birthdate
        self.id = id



