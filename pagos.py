# pagos.py

# Lista para almacenar los pagos realizados
pagos = []

def registrar_pago(paciente, monto):
    """
    Registra un nuevo pago en el sistema.
    """
    if not paciente.strip():
        print("Error: El nombre del paciente no puede estar vacío.")
        return
    
    if not isinstance(monto, (int, float)) or monto <= 0:
        print("Error: El monto debe ser un número positivo.")
        return

    pago = {
        "paciente": paciente,
        "monto": monto
    }
    pagos.append(pago)
    print(f"Pago registrado para {paciente} por un monto de ${monto}.")

def modificar_pago(indice, nuevo_monto):
    """
    Modifica el monto de un pago existente.
    """
    if indice < 0 or indice >= len(pagos):
        print("Error: Índice de pago no válido.")
        return

    if not isinstance(nuevo_monto, (int, float)) or nuevo_monto <= 0:
        print("Error: Monto no válido.")
        return

    pagos[indice]["monto"] = nuevo_monto
    print(f"Pago actualizado: {pagos[indice]}")

def mostrar_pagos():
    """
    Muestra todos los pagos registrados.
    """
    if not pagos:
        print("No hay pagos registrados.")
        return
    
    print("\nPagos registrados:")
    for i, pago in enumerate(pagos):
        print(f"{i}: {pago['paciente']} - Monto: ${pago['monto']}")

def mostrar_pagos_pendientes():
    """
    Muestra los pagos pendientes.
    (Funcionalidad pendiente de implementar con tratamientos)
    """
    print("\nFuncionalidad de pagos pendientes no implementada aún.")


