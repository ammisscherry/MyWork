from Objetos.Cliente import Cliente
from Objetos.ClienteFrecuente import ClienteFrecuente

class RegistroClientes:
    def __init__(self):
        self._clientes = []

    def registrar_cliente(self, nombre, correo):
        cliente = Cliente(nombre, correo)
        self._clientes.append(cliente)
        return f"Cliente '{nombre}' registrado."

    def registrar_cliente_frecuente(self, nombre, correo, num_visitas):
        cliente = ClienteFrecuente(nombre, correo, num_visitas)
        self._clientes.append(cliente)
        return f"Cliente frecuente '{nombre}' registrado."

    def buscar_cliente(self, nombre):
        for cliente in self._clientes:
            if cliente._nombre == nombre:
                return cliente
        return None

    def __str__(self):
        if not self._clientes:
            return "No hay clientes registrados."
        return "\n".join(str(c) for c in self._clientes)
