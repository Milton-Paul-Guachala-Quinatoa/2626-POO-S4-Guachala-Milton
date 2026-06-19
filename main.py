# Importar las clases del proyecto
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante("Sabor Ecuatoriano")

# Crear productos
producto1 = Producto("Encebollado", 3.50, "Sopa")
producto2 = Producto("Hornado", 7.00, "Plato fuerte")
producto3 = Producto("Morocho", 1.00, "Bebida")

# Crear clientes
cliente1 = Cliente("José Pacheco", "0991234567")
cliente2 = Cliente("Andrés Crespo", "0987654321")

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar la información registrada
print("=== SISTEMA DE GESTIÓN DE RESTAURANTE ===")
print(f"Nombre del restaurante: {restaurante.nombre}")

print("\n=== PRODUCTOS ===")
for producto in restaurante.productos:
    print(producto)

print("\n=== CLIENTES ===")
for cliente in restaurante.clientes:
    print(cliente)