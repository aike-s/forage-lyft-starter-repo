from abc import ABC, abstractmethod


class Battery(ABC):
    """ Battery base class """

    @abstractmethod
    def needs_service(self):
        pass
