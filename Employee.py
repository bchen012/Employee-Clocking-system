class Employee:
    def __init__(self, id, name, clockedIn = "no"):   #if clockedIn is placed, it will be that value, else, default to "no"
        self.id = id
        self.name = name
        self.clockedIn = clockedIn

