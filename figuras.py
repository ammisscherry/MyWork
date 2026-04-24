from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

    def mostrar_info(self):
        return (
            f"{type(self).__name__} "
            f"Área: {self.area():.2f}, "
            f"Perímetro: {self.perimetro():.2f}"
        )




