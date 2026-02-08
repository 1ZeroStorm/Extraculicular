from abc import ABC, abstractmethod

class createobjsample(ABC):
    def __init__(self, att1):
        self.att1 = att1

    @abstractmethod
    def op1(self):
        pass

    @abstractmethod
    def op2(self):
        pass

    @abstractmethod
    def op3(self):
        pass