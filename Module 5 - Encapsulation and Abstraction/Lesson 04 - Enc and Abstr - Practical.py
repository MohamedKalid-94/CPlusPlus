from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self):
        self.__engine_temp = 90  # Encapsulated variable

    def start_engine(self):
        print("Engine started...")

    def get_engine_temp(self):
        return self.__engine_temp

car = Car()
car.start_engine()
print("Engine Temp:", car.get_engine_temp())
