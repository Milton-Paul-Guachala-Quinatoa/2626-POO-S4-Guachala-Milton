# Sistema de Gestión de Restaurante

## Nombre del estudiante

**Milton Paul Guachala Quinatoa**

## Descripción del sistema

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos y clientes, organizando el código en diferentes módulos para demostrar el uso de clases, objetos, constructores, atributos, métodos, el método especial `__str__()` e importaciones entre archivos.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```text
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

* **modelos/**: Contiene las clases `Producto` y `Cliente`, que representan las entidades principales del sistema.
* **servicios/**: Contiene la clase `Restaurante`, encargada de administrar los productos y clientes registrados.
* **main.py**: Es el archivo principal donde se crean los objetos, se agregan al restaurante y se muestra la información en la consola.

## Reflexión

La modularización permite organizar mejor el código, facilitando su lectura, mantenimiento y reutilización. Separar las responsabilidades en diferentes archivos hace que cada clase cumpla una función específica, lo que mejora la comprensión y el desarrollo de programas utilizando Programación Orientada a Objetos.
