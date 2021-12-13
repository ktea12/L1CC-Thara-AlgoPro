#Thara L1CC (2502046944)

class Person:
    def __init__(self, name="Rin", address="Konoha"):
        self.__name = name
        self.__address = address
    
    def setName (self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setAddress(self, address):
        self.__address = address
    
    def getAddress(self):
        return self.__address

    def __str__ (self):
        return f"Name: {self.getName()}\nAddress: {self.getAddress()}"


print(Person())
    

class Student(Person):
    
    def __init__(self, name, address, numCourses= 0, courses=[], grades=[]):
        super().__init__(name, address)
        self.__name = name
        self.__address = address
        self.__numCourses = numCourses
        self.__courses = courses
        self.__grades = grades   

    def addCourseGrade(self, numCourses, courses, grades):
        self.__numCourses = input("Number of courses: ")
        
        self.__courses = courses
        new_course = input("Course name: ")
        self.__courses.append(new_course)
         
        self.__grades = grades   
        new_grades = int(input("Grade: "))
        self.__grades.append(new_grades)
            
        return self.__courses, self.__grades
    
    def printGrades(self):
       return self.__grades
        
    def __str__(self):
        return f"Student Name: {self.__name}\nAddress: {self.__address}\nCourse: {self.__courses()}\nGrade: {self.printGrades()}"

print(Student())

class Teacher(Person):

    def __init__(self, name, address, numCourses=0, courses[]):
        super().__init__(name, address)
        self.__name = name
        self.__address = address
        self.__numCourses = numCourses
        self.__courses = courses
    
    def addCourse(self):
        bool(self.__courses)
        
    def removeCourse(self):
        bool(self.__courses)
        
    def __str__(self):
        return f"Teacher Name: {self.__name}\nAddress: {self.__address}\nCourse: {self.__courses()}"