# registro_citas.py
import re

# Lista para almacenar las citas
citas = []

def validar_fecha(fecha):
    """ Verifica que la fecha tenga el formato YYYY-MM-DD """
    patron = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(patron, fecha))

def validar_hora(hora):
    """ Verifica que la hora tenga el formato HH:MM """
    patron = r"^\d{2}:\d{2}$"
    return bool(re.match(patron, hora))

def agregar_cita(paciente, fecha, hora, motivo):
    """
    Agrega una nueva cita al sistema.
    """
    if not validar_fecha(fecha):
        print("Error: La fecha debe estar en formato YYYY-MM-DD.")
        return
    
    if not validar_hora(hora):
        print("Error: La hora debe estar en formato HH:MM.")
        return
    
    if not motivo.strip():
        print("Error: El motivo no puede estar vacío.")
        return

    cita = {
        "paciente": paciente,
        "fecha": fecha,
        "hora": hora,
        "motivo": motivo
    }
    citas.append(cita)
    print(f"Cita agregada para {paciente} el {fecha} a las {hora}.")

def modificar_cita(indice, nueva_fecha=None, nueva_hora=None, nuevo_motivo=None):
    """
    Modifica una cita existente.
    """
    if indice < 0 or indice >= len(citas):
        print("Error: Índice de cita no válido.")
        return
    
    cita = citas[indice]

    if nueva_fecha:
        if not validar_fecha(nueva_fecha):
            print("Error: Fecha no válida.")
            return
        cita["fecha"] = nueva_fecha

    if nueva_hora:
        if not validar_hora(nueva_hora):
            print("Error: Hora no válida.")
            return
        cita["hora"] = nueva_hora

    if nuevo_motivo:
        cita["motivo"] = nuevo_motivo

    print(f"Cita modificada: {cita}")

def cancelar_cita(indice):
    """
    Cancela una cita del sistema.
    """
    if indice < 0 or indice >= len(citas):
        print("Error: Índice de cita no válido.")
        return

    cita_cancelada = citas.pop(indice)
    print(f"Cita cancelada: {cita_cancelada}")

def mostrar_citas():
    """
    Muestra todas las citas registradas.
    """
    if not citas:
        print("No hay citas registradas.")
        return
    
    print("\nCitas registradas:")
    for i, cita in enumerate(citas):
        print(f"{i}: {cita['paciente']} - {cita['fecha']} a las {cita['hora']} - {cita['motivo']}")
