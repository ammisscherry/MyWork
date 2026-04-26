from Objetos.Producto import Producto

class RegistroProductos:
    def __init__(self):
        self._productos = []

    def registrar_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        self._productos.append(producto)
        return f"Producto '{nombre}' registrado."

    def buscar_producto(self, nombre):
        for producto in self._productos:
            if producto.getNombre() == nombre:
                return producto
        return None

    def __str__(self):
        if not self._productos:
            return "No hay productos registrados."
        return "\n".join(str(p) for p in self._productos)
