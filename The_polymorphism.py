## poly (Many) + morphe (form)
## in programming, plymorphism is describes the ability of an object  to take on many forms.
## AM it allows diffrent objects to be accessed through a uniform interface.
### Where a single interface can be used for a different types of objects.

## We have two ways to achieve polymorphism in pyhthon.
## 1 . we have a method called Overriding.
##    > it is used with inheritance
######  Where the child class provides a specific implementation of a method that is already defined in its parent class.

## 2  . we have a method of Duck Typing.
#####  > Unique to Dynamic language like python.
#### here we donot care about the type of object, we only care about the method we are calling on the object.



### This is an example of the first method of polymorphism called Overriding.
class Animal:
    def speak(self):
        print("Some generic sound")
        
class Dog(Animal):
    def speak(self):
        print("Woof!")     ## overrides parent methood.
        
class cat(Animal):
    def speak(self):
        print("Meow!")      ## overrides parent method.
        
### Polymorphism in action
animal = (Dog(), cat(), Animal())

for animal in animal:
    animal.speak()          ## call the specific version for each object.