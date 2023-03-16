from abc import ABC, abstractmethod


class Engine(ABC):
    """ Engine base class """

    @abstractmethod
    def needs_service(self):
        pass
