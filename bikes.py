class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Price: " + str(self.price) 
        print "Max Speed: " + str(self.max_speed)
        print "Total Miles: " + str(self.miles)
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self


bike1= Bike(200, "25mph", 30)
bike2= Bike(300, "30pmh", 75)
bike3= Bike(500, "100mph", 120)

print bike1.ride().displayInfo()
print bike2.reverse().displayInfo()
print bike3.ride().reverse().displayInfo()




