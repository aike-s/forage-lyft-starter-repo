from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery

    @abstractmethod
    def needs_service(self):
        pass
