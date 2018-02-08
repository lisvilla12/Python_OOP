class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -=1
        return self
    def run(self):
        self.health -=5
        return self
    def displayHealth(self):
        print "Name: " + str(self.name)
        print "Health report: " + str(self.health) + "%"
        return self

class dog(Animal):
    def __init__(self,name):
        super (dog, self).__init__(name, 150)
    def pet(self):
        self.health +=5
        return self

class dragon(Animal):
    def __init__(self, name):
        super(dragon, self).__init__(name, 170)
    def fly(self):
        self.health +=10
        return self
    def displayHealth(self):
        print "Name: " + str(self.name) + " the Dragon"
        print "Health report: " + str(self.health) + "%"
        return self


x = Animal("Jazz")
x.walk().walk().walk().run().run().displayHealth()

y = dog("Abby")
y.walk().walk().walk().run().run().pet().displayHealth()

#proves dog can't fly
#d=dog("Spike")
#d.fly().displayHealth()

z = dragon("Sky")
z.fly().displayHealth()
