# Clase que representa un producto del restaurante

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    # Devuelve la información del producto en formato de texto
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} ({self.categoria})"