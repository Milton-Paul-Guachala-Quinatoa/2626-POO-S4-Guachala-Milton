# Clase que representa un cliente del restaurante

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    # Devuelve la información del cliente en formato de texto
    def __str__(self):
        return f"{self.nombre} - Teléfono: {self.telefono}"