import random

class Car:
    def __init__(self, reg_number, max_speed):
        self.regNumber = reg_number
        self.maxSpeed = max_speed
        self.curr_speed = 0
        self.travDist= 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        new_speed = self.curr_speed + speed_change

        self.curr_speed = max(0, min(new_speed, self.maxSpeed))

    def drive(self, hours=1):

        self.travDist += self.curr_speed * hours

def start_race():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        car = Car(f"ABC-{i}", max_speed)
        cars.append(car)

    race_ongoing = True
    hour = 0

    while race_ongoing:
        hour += 1
        print(f"--- Hour {hour} ---")

        for car in cars:
            car.accelerate()
            car.drive()

            if car.travDist >= 10000:
                race_ongoing = False
                break

    print(
        f"\n{'Reg num':<10} {'Max Speed (km/h)':<18} {'Current Speed (km/h)':<20} {'Distance Travelled (km)':<20}")
    print("-" * 70)
    for car in cars:
        print(f"{car.regNumber:<10} {car.maxSpeed:<18} {car.curr_speed:<20} {car.travDist:<20.2f}")

start_race()
