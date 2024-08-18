from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        """this method should be implemented!"""

    @abstractmethod
    def repair(self):
        """this method should be implemented!"""

    def class_name(self):
        print(self.__class__)


class LandVehicle(Vehicle):
    @abstractmethod
    def brake(self):
        """this method should be implemented!"""


class AirVehicle(Vehicle):
    @abstractmethod
    def eject(self):
        """this method should be implemented!"""


class Car(LandVehicle):
    def move(self):
        print("driving....")

    def repair(self):
        print("under repair0000")

    def brake(self):
        print("braking....")


class AirPlane(AirVehicle):
    def move(self):
        print("flying....")

    def repair(self):
        print("under repair....")

    def eject(self):
        print("ejecting....")


a = AirPlane()
a.class_name()
a.repair()
a.move()
a.eject()
