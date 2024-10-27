# Exercise 2
from asyncio import current_task


class Car:
    def __init__(self, reg_number, max_speed, curr_speed=0, trav_dist=0):
        self.max_speed = max_speed
        self.reg_number = reg_number
        self.curr_speed = curr_speed
        self.trav_dist = trav_dist

    def accelerate(self, speed):
        self.curr_speed += speed
        if speed > self.max_speed:
                self.curr_speed = self.max_speed
        elif speed < 0:
                speed = 0
                self.curr_speed = speed

car = Car(curr_speed=0, trav_dist=0, reg_number="ABC-123", max_speed=142,)

print(f"Registration number: {car.reg_number}")
print(f"Current speed: {car.curr_speed}km/h")
print(f"Starting travel distance: {car.trav_dist}km")
print(f"Maximum speed: {car.max_speed}km/h")

car.accelerate(30)
print(f"If speed given is 30km/h, current speed will be {car.curr_speed}km/h.")
car.accelerate(70)
print(f"If speed given is 50km/h, current speed will be {car.curr_speed}km/h.")
car.accelerate(150)
print(f"current speed is: {car.curr_speed}km/h.")
car.accelerate(-200)
print(f"If speed given is -200km/h, current speed will be {car.curr_speed}km/h.")

