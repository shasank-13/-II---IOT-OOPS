class Vehicle:
     def describe(self):
          print("This is a generic vehicle.")
class Car(Vehicle):
        print("This  is a BMW car.")
class Motorcycle(Vehicle):
     def describe(self):
          print("This is a fast motorcycle.")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
