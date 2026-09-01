# Create a class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

# Create an object
p1 = Person("Pop", 46)

# Call the greet method
p1.greet()


###########
#THE CHECK LIST
#✓
#Create class Person
#✓
#Add __init__ method with name and age
#✓
#Add greet method
#✓
#Create object p1 with "Pop" and 46
#✓
#Call p1.greet()
#################################################################################