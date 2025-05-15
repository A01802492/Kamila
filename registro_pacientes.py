# registro_pacientes.py

# Lista para almacenar los datos de los pacientes
pacientes = []

def registrar_paciente(nombre, edad, direccion):
    """
    Registra un nuevo paciente en el sistema.
    """
    if not nombre.strip():
        print("Error: El nombre no puede estar vacío.")
        return
    
    if not isinstance(edad, int) or edad <= 0:
        print("Error: La edad debe ser un número entero positivo.")
        return
    
    if not direccion.strip():
        print("Error: La dirección no puede estar vacía.")
        return

    paciente = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion
    }
    pacientes.append(paciente)
    print(f"Paciente {nombre} registrado correctamente.")

def modificar_paciente(indice, nuevo_nombre=None, nueva_edad=None, nueva_direccion=None):
    """
    Modifica los datos de un paciente existente.
    """
    if indice < 0 or indice >= len(pacientes):
        print("Error: Índice de paciente no válido.")
        return

    paciente = pacientes[indice]

    if nuevo_nombre:
        paciente["nombre"] = nuevo_nombre

    if nueva_edad:
        if not isinstance(nueva_edad, int) or nueva_edad <= 0:
            print("Error: Edad no válida.")
            return
        paciente["edad"] = nueva_edad

    if nueva_direccion:
        paciente["direccion"] = nueva_direccion

    print(f"Paciente modificado: {paciente}")

def mostrar_pacientes():
    """
    Muestra todos los pacientes registrados.
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    print("\nPacientes registrados:")
    for i, paciente in enumerate(pacientes):
        print(f"{i}: {paciente['nombre']} - {paciente['edad']} años - {paciente['direccion']}")
