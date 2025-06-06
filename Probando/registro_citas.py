import re
from datetime import datetime

citas = []

def validar_fecha(fecha):
    """Valida el formato de fecha YYYY-MM-DD"""
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_hora(hora):
    """Valida el formato de hora HH:MM"""
    return bool(re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', hora))

def existe_cita(fecha, hora):
    """Verifica si ya existe una cita en la misma fecha y hora"""
    return any(c['fecha'] == fecha and c['hora'] == hora for c in citas)

def agregar_cita(paciente, fecha, hora, motivo):
    """Agrega una nueva cita"""
    if not validar_fecha(fecha):
        raise ValueError("Formato de fecha incorrecto (debe ser AAAA-MM-DD)")
    
    if not validar_hora(hora):
        raise ValueError("Formato de hora incorrecto (debe ser HH:MM)")
    
    if not motivo.strip():
        raise ValueError("El motivo no puede estar vacío")
    
    cita = {
        'paciente': paciente,
        'fecha': fecha,
        'hora': hora,
        'motivo': motivo,
        'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    citas.append(cita)

def modificar_cita(indice, nueva_fecha=None, nueva_hora=None, nuevo_motivo=None):
    """Modifica una cita existente"""
    if indice < 0 or indice >= len(citas):
        raise IndexError("Índice de cita no válido")
    
    if nueva_fecha and not validar_fecha(nueva_fecha):
        raise ValueError("Formato de fecha incorrecto")
    
    if nueva_hora and not validar_hora(nueva_hora):
        raise ValueError("Formato de hora incorrecto")
    
    if nuevo_motivo and not nuevo_motivo.strip():
        raise ValueError("El motivo no puede estar vacío")
    
    if nueva_fecha:
        citas[indice]['fecha'] = nueva_fecha
    if nueva_hora:
        citas[indice]['hora'] = nueva_hora
    if nuevo_motivo:
        citas[indice]['motivo'] = nuevo_motivo

def cancelar_cita(indice):
    """Cancela una cita"""
    if indice < 0 or indice >= len(citas):
        raise IndexError("Índice de cita no válido")
    return citas.pop(indice)

def mostrar_citas():
    """Muestra todas las citas programadas"""
    if not citas:
        print("No hay citas registradas")
        return
    
    print("\nLISTA DE CITAS")
    print("-" * 80)
    print(f"{'ID':<5}{'PACIENTE':<20}{'FECHA':<12}{'HORA':<8}{'MOTIVO':<30}{'REGISTRO':<20}")
    print("-" * 80)
    
    for i, c in enumerate(citas):
        print(f"{i:<5}{c['paciente']:<20}{c['fecha']:<12}{c['hora']:<8}{c['motivo']:<30}{c.get('fecha_registro', 'N/D'):<20}")