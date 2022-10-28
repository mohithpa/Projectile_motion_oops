import matplotlib.pyplot as plt 
import math
import numpy as np

class Projectile:
    def __init__(self, theta: float, g: float, u: float):
        # Run validations to the received arguments/ Assert values
        assert theta >= 0 and theta <= 360, f"theta {theta} is not in asserted range!"
        assert u >= 0, f"intitial velocity {u} is less than 0, please check!"

        # Assign to self object
        print("i am created")
        self.g = g
        self.theta = (np.pi/180)*theta
        self.u = u

    def tof(self):
        time_of_flight = (2*self.u*np.sin(self.theta))/self.g
        return time_of_flight

    def range_of_flight(self):
        distance = ((self.u**2)*np.sin(2*self.theta))/self.g

    def build_time_array(self):
        a = self.tof()
        return np.linspace(0,a,100)

    def x_y_calc(self):
        time_array = self.build_time_array()
        x = []
        y = []
        for t in time_array:
            xval = self.u*t*np.cos(self.theta)
            yval = (self.u*np.sin(self.theta)*t)-(0.5*self.g*t**2)
            x.append(xval)
            y.append(yval)
        return x, y

projectile1 = Projectile(45, 9.8, u = 20 )
a,b = projectile1.x_y_calc()
print(Projectile.__dict__) # All the attributes of the class level
print(projectile1.__dict__) # All the attributes for the instance level
print(a)
print(b)
plt.plot(a,b)
plt.savefig("oops.png")
