from datetime import datetime

pacientes = []

def existe_paciente(nombre):
    """Verifica si un paciente ya existe"""
    return any(p['nombre'].lower() == nombre.lower() for p in pacientes)

def registrar_paciente(nombre, edad, direccion):
    """Registra un nuevo paciente"""
    paciente = {
        'nombre': nombre,
        'edad': edad,
        'direccion': direccion,
        'fecha_registro': datetime.now().strftime("%Y-%m-%d")
    }
    pacientes.append(paciente)

def modificar_paciente(indice, nuevo_nombre=None, nueva_edad=None, nueva_direccion=None):
    """Modifica los datos de un paciente"""
    if indice < 0 or indice >= len(pacientes):
        raise IndexError("Índice de paciente no válido")
    
    if nuevo_nombre:
        pacientes[indice]['nombre'] = nuevo_nombre
    if nueva_edad:
        pacientes[indice]['edad'] = nueva_edad
    if nueva_direccion:
        pacientes[indice]['direccion'] = nueva_direccion

def eliminar_paciente(indice):
    """Elimina un paciente del sistema"""
    if indice < 0 or indice >= len(pacientes):
        raise IndexError("Índice de paciente no válido")
    return pacientes.pop(indice)

def mostrar_pacientes():
    """Muestra todos los pacientes registrados"""
    if not pacientes:
        print("No hay pacientes registrados")
        return
    
    print("\nLISTA DE PACIENTES")
    print("-" * 50)
    print(f"{'ID':<5}{'NOMBRE':<20}{'EDAD':<10}{'DIRECCIÓN':<20}{'REGISTRO':<15}")
    print("-" * 50)
    
    for i, p in enumerate(pacientes):
        print(f"{i:<5}{p['nombre']:<20}{p['edad']:<10}{p['direccion']:<20}{p.get('fecha_registro', 'N/D'):<15}")
