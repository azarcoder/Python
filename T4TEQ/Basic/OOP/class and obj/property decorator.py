class celsius:
    def __init__(self,t=0):
        self.temperature=t
    def to_fahr(self):
        return (self.temperature * 1.8)+32

    @property
    def temperature(self):
        print('Getting value...')
        return self.__temperature

    @temperature.setter
    def temperature(self,value):
        print('setting value...')
        if value< -273.15:
            raise ValueError("Temperature below 273.15 is not possible")
        self.__temperature = value

h = celsius(37)
print(h.temperature)
print(h.to_fahr())
