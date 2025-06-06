from datetime import datetime

pagos = []

def registrar_pago(paciente, tratamiento, monto, fecha):
    """Registra un nuevo pago"""
    pago = {
        'paciente': paciente,
        'tratamiento': tratamiento,
        'monto': monto,
        'fecha': fecha,
        'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    pagos.append(pago)

def modificar_pago(indice, nuevo_monto=None, nueva_fecha=None):
    """Modifica un pago existente"""
    if indice < 0 or indice >= len(pagos):
        raise IndexError("Índice de pago no válido")
    
    if nuevo_monto:
        pagos[indice]['monto'] = nuevo_monto
    if nueva_fecha:
        pagos[indice]['fecha'] = nueva_fecha

def eliminar_pago(indice):
    """Elimina un pago"""
    if indice < 0 or indice >= len(pagos):
        raise IndexError("Índice de pago no válido")
    return pagos.pop(indice)

def mostrar_pagos():
    """Muestra todos los pagos"""
    if not pagos:
        print("No hay pagos registrados")
        return
    
    print("\nLISTA DE PAGOS")
    print("-" * 80)
    print(f"{'ID':<5}{'PACIENTE':<20}{'TRATAMIENTO':<25}{'MONTO':<15}{'FECHA':<15}")
    print("-" * 80)
    
    for i, p in enumerate(pagos):
        print(f"{i:<5}{p['paciente']:<20}{p['tratamiento']:<25}${p['monto']:<15.2f}{p['fecha']:<15}")

def mostrar_pagos_pendientes():
    """Muestra los pagos pendientes"""
    # Esta función necesitaría integración con citas y tratamientos
    # para determinar qué pagos están pendientes
    print("\nFUNCIONALIDAD EN DESARROLLO")
    print("Esta función mostrará los pagos pendientes en futuras versiones")