# Exercise 3
class Car:
    def __init__(self, reg_number, max_speed):
        self.currSpeed = 60
        self.travDist = 2000
        self.maxSpeed = max_speed
        self.regNumber = reg_number

    def accelerate(self, speed):
        if speed > self.maxSpeed:
            speed = self.maxSpeed
        elif speed < 0:
                speed = 0
        self.currSpeed = speed
    def drive(self,hours):
        self.travDist = self.travDist + (hours * self.currSpeed)

car = Car(reg_number="ABC-123", max_speed=142)

print(f"Registration number: {car.regNumber}")
print(f"Current speed: {car.currSpeed}km/h")
print(f"Starting travel distance: {car.travDist}km")
print(f"Maximum speed: {car.maxSpeed}km/h")

car.drive(1.5)
print(f"The total distance after 90 minutes of travel: {car.travDist}km")
