# tratamientos_precios.py

# Lista para almacenar los tratamientos y sus precios
tratamientos = []

def registrar_tratamiento(nombre, precio):
    """
    Registra un nuevo tratamiento en el sistema.
    """
    if not nombre.strip():
        print("Error: El nombre del tratamiento no puede estar vacío.")
        return
    
    if not isinstance(precio, (int, float)) or precio <= 0:
        print("Error: El precio debe ser un número positivo.")
        return

    tratamiento = {
        "nombre": nombre,
        "precio": precio
    }
    tratamientos.append(tratamiento)
    print(f"Tratamiento '{nombre}' registrado correctamente con precio {precio}.")

def modificar_tratamiento(indice, nuevo_nombre=None, nuevo_precio=None):
    """
    Modifica los datos de un tratamiento existente.
    """
    if indice < 0 or indice >= len(tratamientos):
        print("Error: Índice de tratamiento no válido.")
        return

    tratamiento = tratamientos[indice]

    if nuevo_nombre:
        tratamiento["nombre"] = nuevo_nombre

    if nuevo_precio:
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio <= 0:
            print("Error: Precio no válido.")
            return
        tratamiento["precio"] = nuevo_precio

    print(f"Tratamiento modificado: {tratamiento}")

def mostrar_tratamientos():
    """
    Muestra todos los tratamientos registrados.
    """
    if not tratamientos:
        print("No hay tratamientos registrados.")
        return
    
    print("\nTratamientos registrados:")
    for i, tratamiento in enumerate(tratamientos):
        print(f"{i}: {tratamiento['nombre']} - Precio: ${tratamiento['precio']}")

