class Birthday:

    # Basic constructor
    def __init__(self, month=-111, day=-222):
        self.__month = month
        self.__day = day

    # Mutator for __day
    def set_day(self, day):
        if (day>0 and day<=31):
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
        pass
    
    def __str__(self):
        return f"[ {self.get_month()}/{self.get_day()} ]"
    

if __name__=="__main__":
    leo = Birthday(6,28)
    #leo.month = 6
    leo.set_day(29)
    print(leo)
    print(leo.get_day(), leo.get_month())