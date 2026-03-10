from modelos.libro import Libro
from modelos.user import Usuario
from servicios.gestorPrestamos import GestorPrestamos

libro1=Libro("Pepa Pig","Bucanero","12345")
usuario1=Usuario("Valeria","2521578")

gestor=GestorPrestamos()

mensaje=gestor.realizar_prestamo(libro1,usuario1,"7/3/2026")

print(mensaje)
print(libro1.disponibilidad)

gestor.listar_prestamos()