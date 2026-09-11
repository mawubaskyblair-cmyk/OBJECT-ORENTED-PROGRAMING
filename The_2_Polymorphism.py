class Duck:
    def fly(self):
        print("Duck is flying")
        
class Airplane:
    def fly(self):
        print("Airplane is flying")
        
class whale:
    def swim(self):
        print("whale is swimming")
        
def lift_off(entity):
    # We don,t care about the type, but we just want the behavoir.
    entity.fly()
    
lift_off(Duck())      # Works !
lift_off(Airplane())  # Works !
lift_off(whale())     # Error! No fly() method in whale class.