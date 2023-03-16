from abc import ABC, abstractmethod
from .car import Car
""" IMPORT ENGINES """
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
""" IMPORT BATTERIES """
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory(ABC):

    def create_calliope(self, current_date, last_service_date, current_milleage, last_service_milleage):
        engine = CapuletEngine(last_service_milleage=last_service_milleage, current_milleage=current_milleage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        new_calliope = Car(engine, battery)

        return new_calliope

    def create_glissade(self, current_date, last_service_date, current_milleage, last_service_milleage):
        engine = WilloughbyEngine(last_service_milleage=last_service_milleage, current_milleage=current_milleage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        new_glissade = Car(engine, battery)

        return new_glissade

    def create_palindrome(self, current_date, last_service_date, current_milleage, last_service_milleage):
        engine = SternmanEngine(last_service_milleage=last_service_milleage, current_milleage=current_milleage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        new_palindrome = Car(engine, battery)

        return new_palindrome
    
    def create_rorschach(self, current_date, last_service_date, warning_light_on):
        engine = WilloughbyEngine(warning_light_on=warning_light_on)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        new_rorschach = Car(engine, battery)

        return new_rorschach

    def create_thovex(self, current_date, last_service_date, current_milleage, last_service_milleage):
        engine = CapuletEngine(last_service_milleage=last_service_milleage, current_milleage=current_milleage)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
        new_thovex = Car(engine, battery)

        return new_thovex