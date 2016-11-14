## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal (subclass)
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a feature "name"
        self.name = name

## Cat is-a Animal (subclass)
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a feature "name"
        self.name = name

## Person is-a object (super class)
class Person(object):

    def __init__(self, name):
        ## Person has-a feature "name"
        self.name = name

        ## Person has-a pet some kind
        self.pet = None

##??
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a Person() (subclass)
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object (super class)
class Fish(object):
    pass

## Salmon is-a Fish (subclass)
class Salmon(Fish):
    pass

## Halibut is-a Fish (subclass)
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet called Satan
mary.pet = satan

## Frank is-a Employee with the name Frank and a salary of 120000
frank = Employee("Frank", 120000)

## Frank has-a pet called Rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
