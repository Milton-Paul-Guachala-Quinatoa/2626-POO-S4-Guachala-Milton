# Clase que administra los productos y clientes del restaurante

class Restaurante:

    # Constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # Agrega un producto al restaurante
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Agrega un cliente al restaurante
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)