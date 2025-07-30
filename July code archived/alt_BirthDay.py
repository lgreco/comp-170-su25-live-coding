from datetime import datetime

class Birthday:

    # Basic constructor
    def __init__(self, month=-111, day=-222):
        self.__month = month
        self.__day = day

    # Mutator for __day
    def set_day(self, day):
        if day > 0 and day <= 31:
            self.__day = day

    # Accessor for __month
    def get_month(self):
        return self.__month

    # Accessor for __day
    def get_day(self):
        return self.__day

    # Compute days to birthday
    def days_until(self):
        # obtain today's date
        # extract month and day
        # subtract from birthday
        # return # of days
        bm = self.__month
        bd = self.__day
        bdays = self.days_passed_in_year(bm, bd)
        today = datetime.today()
        tdays = self.days_passed_in_year(today.month, today.day)
        until = tdays - bdays
        if bdays < tdays:
            until = (365 - tdays) + bdays
        return until+1 if (self.is_leap_year(today.year) or self.is_leap_year(today.year+1)) else until

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def days_passed_in_year(self, month, day):
        count = 0
        for i in range(month - 1):
            count += Birthday.days_in_month[i]
        return count + day

    def is_leap_year(self, year):
        return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

    def __str__(self):
        return f"[ {self.get_month()}/{self.get_day()} ]"


if __name__ == "__main__":
    leo = Birthday(6, 28)
    # leo.month = 6
    leo.set_day(29)
    print(leo)
    print(leo.get_day(), leo.get_month())
    # leo.days_left_in_year()
    print(leo.days_until())
