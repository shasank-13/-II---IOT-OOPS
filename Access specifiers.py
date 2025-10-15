class Employee:
   def __init__(self, name,age,salary):
     self.name=name
     self._age=age
     self.__salary=salary

#class SubEmployee(Employee):
   def show_age(self):
       print("Age:", self._age)

   def show_salary(self):
       print("Salary:",self.__salary)
       

emp = Employee("Shasank",19,100000)
print(emp.name)
emp.show_age()
emp.show_salary()

        
