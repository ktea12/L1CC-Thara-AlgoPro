#person, student, and teacher class

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


Person()
    

class Student(Person):
    
    def studentName(Person):
        print(super.Person)
    
    def __init__(self, numCourses= 0, courses=[], grades=[]):
        numCourses = input("Number of courses: ")
        self.__numCourses = numCourses
        self.__courses = courses
        self.__grades = grades
    
    def addCourseGrade(self, numCourses, courses, grades):
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
        return f"Course: {self.__courses()}\nGrade: {self.printGrades()}"

print(Student())

class Teacher(Person):
    
    def studentName(Person):
        print(Person())
