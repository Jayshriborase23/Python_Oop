
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped.")


class Car(Vehicle):

    def start(self):
        print("Car starts with a key or button.")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with a key or self-start.")


car = Car()
bike = Bike()

car.start()
car.stop()

print()

bike.start()
bike.stop()
