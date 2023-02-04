from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self): #abstract method
        pass
    def fff(self):
        print('llll')

class laptop(Computer):
  #  @abstractmethod
    def process(self):
        pass
#s=Computer()
com1 = laptop()
com1.process()
com1.fff()

