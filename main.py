from Cafeteria import Cafeteria
from Utilidades.crear_pedidos import crear_pedido
from Utilidades.calculo_ValorPedido import calcular_valor


cafeteria = Cafeteria("Cafetería Gatitos")
print(cafeteria)
print()

# Registrar clientes
print(cafeteria.registrar_cliente("Nagi", "nagi@gmail.com"))
print(cafeteria.registrar_cliente_frecuente("Valeria", "vale@gmail.com", 15))
print()

# Registrar productos
print(cafeteria.registrar_producto("Café Americano", 35.00))
print(cafeteria.registrar_producto("Pastel de chocolate", 55.00))
print()


pedido1 = crear_pedido(cafeteria, "Nagi")
cafeteria.agregar_producto_a_pedido(pedido1, "Café Americano")
cafeteria.agregar_producto_a_pedido(pedido1, "Pastel de chocolate")
print(pedido1)
print()


pedido2 = crear_pedido(cafeteria, "Valeria")
cafeteria.agregar_producto_a_pedido(pedido2, "Café Americano")
cafeteria.agregar_producto_a_pedido(pedido2, "Pastel de chocolate")
cafeteria.agregar_producto_a_pedido(pedido2, "Pastel de chocolate")
cafeteria.agregar_producto_a_pedido(pedido2, "Pastel de chocolate")
cafeteria.agregar_producto_a_pedido(pedido2, "Pastel de chocolate")
cafeteria.agregar_producto_a_pedido(pedido2, "Pastel de chocolate")
cafeteria.agregar_producto_a_pedido(pedido2, "Pastel de chocolate")
print(pedido2)