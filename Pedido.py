from Objetos.ClienteFrecuente import ClienteFrecuente

class Pedido:
    DESCUENTO = 0.10

    def __init__(self, cliente):
        self._cliente = cliente
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = sum(p.getPrecio() for p in self._productos)
        if isinstance(self._cliente, ClienteFrecuente):
            total -= total * self.DESCUENTO
        return total

    def __str__(self):
        lineas = [f"Pedido de: {self._cliente._nombre}"]
        for p in self._productos:
            lineas.append(f"  - {p}")
        lineas.append(f"Total: ${self.calcular_total():.2f}")
        return "\n".join(lineas)
