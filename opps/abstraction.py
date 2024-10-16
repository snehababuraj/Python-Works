#Abstraction:to hide implemention details or definitions
#abstarct method:methods with no definitions
#ABC:abstract base class

from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Fronx(Car):
    def start(self):
        print("fronx starr method")
    def accelerate(self):
        print("fronx accelerate method")
    def stop(self):
        print("fronx stop method")
fx=Fronx()
fx.start()
