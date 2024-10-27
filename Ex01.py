# Exercise 1
class Car:
    def __init__(self, reg_number, max_speed,curr_speed=0, trav_dist=0, ):
        self.curr_speed = curr_speed
        self.trav_dist = trav_dist
        self.max_speed = max_speed
        self.reg_number = reg_number

car=Car("ABC-123", 142)

print(f"Registration number: {car.reg_number}")
print(f"Current speed: {car.curr_speed}")
print(f"Travel distance: {car.trav_dist}")
print(f"Maximum speed: {car.max_speed}km/h")