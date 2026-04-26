from Registros.registro_clientes import RegistroClientes
from Registros.registro_productos import RegistroProductos
from Pedido import Pedido

class Cafeteria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._registro_clientes = RegistroClientes()
        self._registro_productos = RegistroProductos()
        self._pedidos = []

    def registrar_cliente(self, nombre, correo):
        return self._registro_clientes.registrar_cliente(nombre, correo)

    def registrar_cliente_frecuente(self, nombre, correo, num_visitas):
        return self._registro_clientes.registrar_cliente_frecuente(nombre, correo, num_visitas)

    def registrar_producto(self, nombre, precio):
        return self._registro_productos.registrar_producto(nombre, precio)

    def crear_pedido(self, nombre_cliente):
        cliente = self._registro_clientes.buscar_cliente(nombre_cliente)
        if cliente:
            pedido = Pedido(cliente)
            self._pedidos.append(pedido)
            return pedido
        return None

    def agregar_producto_a_pedido(self, pedido, nombre_producto):
        producto = self._registro_productos.buscar_producto(nombre_producto)
        if producto:
            pedido.agregar_producto(producto)

    def __str__(self):
        return f"Cafetería: {self._nombre}"
