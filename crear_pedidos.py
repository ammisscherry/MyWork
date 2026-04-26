def crear_pedido(cafeteria, nombre_cliente):
    pedido = cafeteria.crear_pedido(nombre_cliente)
    if pedido:
        return pedido
    return f"No se encontró al cliente '{nombre_cliente}'."
