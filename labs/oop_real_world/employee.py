"""
A simple class Employee that inherits attributes from the class Person
"""


class Person(object):

   def __init__(self,name, age):
      self.age = age
      self.name = name
   
   def setAge(age):
      self.age = age   

class Employee(Person):

   def __init__(self, name, age, salary, department):
      Person.__init__(self,name,age)
      self.salary = salary
      self.department = department
   
   def getSalary(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

   def getAge(self):
      print ("Name : ", self.name,  ", Age: ", self.age)


#patrick = Employee('Patrick','26','455433','IT')

#patrick.getAge()

