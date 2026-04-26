from Objetos.Cliente import Cliente

class ClienteFrecuente(Cliente):
    def __init__(self, nombre, correo, num_visitas):
        super().__init__(nombre, correo)
        self._num_visitas = num_visitas

    def actualizar_visitas(self):
        self._num_visitas += 1

    def get_num_visitas(self):
        return self._num_visitas

    def __str__(self):
        return f"{super().__str__()} - Visitas: {self._num_visitas}"
