class Car:
    def __init__(self, model, year, color, speed):
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def __str__(self):
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"

    def __repr__(self):
        return f"Car('{self.model}', {self.year}, '{self.color}', {self.speed})"

    def accelerate(self, increase):
        self.speed += increase
        return None



class ElectricCar(Car):
    def __init__(self, model, year, color, speed, battery_capacity):
        super().__init__(model, year, color, speed)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h, " \
               f"Battery Capacity: {self.battery_capacity} kWh"

    def __repr__(self):
        return f"ElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.battery_capacity})"

    def accelerate(self, increase):
        super().accelerate(increase)
        return f"Electric car accelerates by {increase} km/h, current speed {self.speed}"


class HybridElectricCar(Car):
    def __init__(self, model, year, color, speed, fuel_consumption):
        super().__init__(model, year, color, speed)
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"

    def __repr__(self):
        return f"HybridElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.fuel_consumption})"


class CarFleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def __repr__(self):
        return f'{self.cars}'

    def sort_cars_by_speed(self):
        return sorted(self.cars, key=lambda car: car.speed)


car1 = Car("Sedan", 2022, "Blue", 120)
electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)
car_fleet = CarFleet()
car_fleet.add_car(car1)
car_fleet.add_car(electric_car1)
car_fleet.add_car(hybrid_car1)
car1.accelerate(10)
electric_car1.accelerate(20)
hybrid_car1.accelerate(15)

sorted_cars = car_fleet.sort_cars_by_speed()
for car in sorted_cars:
    print(car)