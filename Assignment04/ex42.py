## Animal is-a object (yes,sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## self has-a name
        self.name = name
        print(f"Dog: {name}")

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## self has-a name
        self.name = name
        print(f"Cat: {name}")


## Person is-a object
class Person(object):

    def __init__(self, name):
        ## self has-a name
        self.name = name
        print(f"Person: {name}")

    def pet_name(self, name, pet):
        ## Person has-a pet of some kind
        self.pet = pet
        print(f"{name} has a pet called {pet.name}")

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee, self has-a name
        super(Employee, self).__init__(name)
        ## self has-a salary
        self.salary = salary
        print(f"Employee: {name}, {salary}")

## Fish is-a object
class Fish(object):

    def __init__(self, name):
        ## self has-a name
        self.name = name
        print(f"Fish: {name}")

## Salmon is-a Fish
class Salmon(Fish):

    def __init__(self, name):
        ## self has-a name
        self.name = name
        print(f"Salmon: {name}")

## Halibut is-a Fish
class Halibut(Fish):

    def __init__(self, name):
        ## self has-a name
        self.name = name
        print(f"Halibut: {name}")


## rover is-a Dog
rover = Dog("Rover")

## mary is-a person
mary = Person("Mary")

## satan is-a Cat
satan = Cat("Satan")

## Mary has-a pet
mary.pet = satan
mary.pet_name("Mary", satan)

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover
frank.pet_name("Frank", rover)

## flipper is-a Fish
flipper = Fish("Flipper")

##crouse is-a Salmon
crouse = Salmon("Crouse")

## Harry is-a Halibut
harry = Halibut("Harry")
