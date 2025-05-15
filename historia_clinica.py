# historia_clinica.py

# Lista para almacenar las historias clínicas
historias_clinicas = []

def agregar_historia_clinica(paciente, diagnostico, tratamiento, observaciones):
    """
    Agrega una nueva historia clínica para un paciente.
    """
    if not paciente.strip():
        print("Error: El nombre del paciente no puede estar vacío.")
        return
    
    if not diagnostico.strip():
        print("Error: El diagnóstico no puede estar vacío.")
        return
    
    historia = {
        "paciente": paciente,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "observaciones": observaciones
    }
    historias_clinicas.append(historia)
    print(f"Historia clínica registrada para {paciente}.")

def modificar_historia_clinica(indice, nuevo_diagnostico=None, nuevo_tratamiento=None, nuevas_observaciones=None):
    """
    Modifica una historia clínica existente.
    """
    if indice < 0 or indice >= len(historias_clinicas):
        print("Error: Índice de historia clínica no válido.")
        return

    historia = historias_clinicas[indice]

    if nuevo_diagnostico:
        historia["diagnostico"] = nuevo_diagnostico

    if nuevo_tratamiento:
        historia["tratamiento"] = nuevo_tratamiento

    if nuevas_observaciones:
        historia["observaciones"] = nuevas_observaciones

    print(f"Historia clínica modificada: {historia}")

def mostrar_historias_clinicas():
    """
    Muestra todas las historias clínicas registradas.
    """
    if not historias_clinicas:
        print("No hay historias clínicas registradas.")
        return
    
    print("\nHistorias clínicas registradas:")
    for i, historia in enumerate(historias_clinicas):
        print(f"{i}: {historia['paciente']} - Diagnóstico: {historia['diagnostico']} - Tratamiento: {historia['tratamiento']} - Observaciones: {historia['observaciones']}")
