from modelos.libro import Libro
from modelos.prestamo import Prestamo

class GestorPrestamos:
    def __init__(self):
        self.prestamos=[]

    def realizar_prestamo(self, libro, user, fecha):
        if libro.prestar():
            prestamo=Prestamo(libro,user,fecha)
            self.prestamos.append(prestamo)
            return "Prestamo realizado con exito."
        return "El libro no esta disponible."

    def listar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo)