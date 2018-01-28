## Animal is-a object (yes,sort of confusing) look at the extra credit
class Pet(object):
    pass

## Dog is-a Animal
class Dog(Pet):

    def __init__(self, name):
        ## self has-a name
        self.name = name
        print(f"Dog: {name}")

## Cat is-a Animal
class Cat(Pet):

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
        Pet.__init__(pet)
        print(f"So {name} has a pet called {pet}")

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
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## Mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

##crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
