from vehicle import Vehicle
from car import Car

my_vehicle = Vehicle("Toyota", "Corolla", 2022)
my_car = Car("Honda", "Civic", 2023, 4)

print(my_vehicle.make)          
my_vehicle.start_engine()
print(my_car.make)              
print(my_car.num_doors)         
my_car.accelerate()     
