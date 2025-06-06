from datetime import datetime

historias_clinicas = []

def agregar_historia_clinica(paciente, diagnostico, tratamiento, observaciones, fecha):
    """Agrega un registro a la historia clínica"""
    registro = {
        'paciente': paciente,
        'diagnostico': diagnostico,
        'tratamiento': tratamiento,
        'observaciones': observaciones,
        'fecha': fecha,
        'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    historias_clinicas.append(registro)

def modificar_historia_clinica(indice, nuevo_diagnostico=None, nuevo_tratamiento=None, nuevas_observaciones=None, nueva_fecha=None):
    """Modifica un registro de historia clínica"""
    if indice < 0 or indice >= len(historias_clinicas):
        raise IndexError("Índice de registro no válido")
    
    if nuevo_diagnostico:
        historias_clinicas[indice]['diagnostico'] = nuevo_diagnostico
    if nuevo_tratamiento:
        historias_clinicas[indice]['tratamiento'] = nuevo_tratamiento
    if nuevas_observaciones:
        historias_clinicas[indice]['observaciones'] = nuevas_observaciones
    if nueva_fecha:
        historias_clinicas[indice]['fecha'] = nueva_fecha

def eliminar_historia_clinica(indice):
    """Elimina un registro de historia clínica"""
    if indice < 0 or indice >= len(historias_clinicas):
        raise IndexError("Índice de registro no válido")
    return historias_clinicas.pop(indice)

def mostrar_historias_clinicas():
    """Muestra todos los registros de historias clínicas"""
    if not historias_clinicas:
        print("No hay registros en las historias clínicas")
        return
    
    print("\nHISTORIAS CLÍNICAS")
    print("-" * 100)
    print(f"{'ID':<5}{'PACIENTE':<20}{'FECHA':<12}{'DIAGNÓSTICO':<30}{'TRATAMIENTO':<25}{'OBSERVACIONES':<30}")
    print("-" * 100)
    
    for i, h in enumerate(historias_clinicas):
        print(f"{i:<5}{h['paciente']:<20}{h['fecha']:<12}{h['diagnostico']:<30}{h['tratamiento']:<25}{h['observaciones']:<30}")