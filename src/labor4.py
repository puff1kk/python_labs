class Farm:
    def __init__(self, geoloc=None , number=0, fan_power=0):
        self.__geoloc = geoloc
        self.__number = number
        self.__fan_power = fan_power
        self.num = 10
        self.line = "test"

    def get_geoloc(self):
        return self.__geoloc

    def get_number(self):
        return self.__number

    def get_fan_power(self):
        return self.__fan_power

    def __str__(self):
        return f"Farm: {self.__geoloc}"

    def __repr__(self):
        return f"Farm({self.__geoloc}, {self.__number}, {self.__fan_power})"

    def __del__(self):
        print('Об\'єкт видалено')


if __name__ == '__main__':
    a = Farm('123', 24, 5)
    b = Farm('456', 24, 5)
    c = Farm()

print(a.number)
