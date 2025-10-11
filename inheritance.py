class Animal:
   def __init__(self,name):
     self.name=name

   def speak(self):
     return "Generic animal sound"

class Dog(Animal):
   def __init__(self,name,breed):
     super().__init__(name)
     self.breed=breed
   
   def speak(self):
     return "woof!"
   
   def fetch(self):
     return f"{self.name} is fetching the ball."

my_dog=Dog("Buddy","Golden Retriever")

print(f"Name: {my_dog.name}")
print(f"Breed: {my_dog.breed}")
print(my_dog.speak())
print(my_dog.fetch())
