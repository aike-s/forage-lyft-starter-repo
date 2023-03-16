from .battery import Battery
from dateutil.relativedelta import relativedelta


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        time_comparison = relativedelta(self.__last_service_date, self.__current_date).years

        if time_comparison >= 2:
            return True
        else:
            return False

