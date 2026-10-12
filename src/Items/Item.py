from abc import ABC, abstractmethod

class Item(ABC):

    def __int__(self):
        super().__init__()

        self.name:str
        self.price:int
        self.description:str

    @abstractmethod
    def hability(self)->None:
        pass