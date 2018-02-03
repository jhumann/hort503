class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
# implicit inheritance, inherits parent behavior
son.implicit()

dad.override()
# override, will use override under child
son.override()

dad.altered()
# will first run under child function, but then is altered to run under parent and child
son.altered()
