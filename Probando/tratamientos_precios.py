tratamientos = []

def existe_tratamiento(nombre):
    """Verifica si ya existe un tratamiento con ese nombre"""
    return any(t['nombre'].lower() == nombre.lower() for t in tratamientos)

def registrar_tratamiento(nombre, precio):
    """Registra un nuevo tratamiento"""
    if existe_tratamiento(nombre):
        raise ValueError("Ya existe un tratamiento con ese nombre")
    
    tratamiento = {
        'nombre': nombre,
        'precio': precio,
        'fecha_registro': datetime.now().strftime("%Y-%m-%d")
    }
    tratamientos.append(tratamiento)

def modificar_tratamiento(indice, nuevo_nombre=None, nuevo_precio=None):
    """Modifica un tratamiento existente"""
    if indice < 0 or indice >= len(tratamientos):
        raise IndexError("Índice de tratamiento no válido")
    
    if nuevo_nombre:
        if existe_tratamiento(nuevo_nombre) and nuevo_nombre.lower() != tratamientos[indice]['nombre'].lower():
            raise ValueError("Ya existe un tratamiento con ese nombre")
        tratamientos[indice]['nombre'] = nuevo_nombre
    
    if nuevo_precio:
        tratamientos[indice]['precio'] = nuevo_precio

def eliminar_tratamiento(indice):
    """Elimina un tratamiento"""
    if indice < 0 or indice >= len(tratamientos):
        raise IndexError("Índice de tratamiento no válido")
    return tratamientos.pop(indice)

def mostrar_tratamientos():
    """Muestra todos los tratamientos"""
    if not tratamientos:
        print("No hay tratamientos registrados")
        return
    
    print("\nLISTA DE TRATAMIENTOS")
    print("-" * 50)
    print(f"{'ID':<5}{'NOMBRE':<25}{'PRECIO':<15}{'REGISTRO':<15}")
    print("-" * 50)
    
    for i, t in enumerate(tratamientos):
        print(f"{i:<5}{t['nombre']:<25}${t['precio']:<15.2f}{t.get('fecha_registro', 'N/D'):<15}")