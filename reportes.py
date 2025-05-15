# reportes.py
from datetime import datetime

# Importamos los módulos necesarios
import pagos
import registro_citas

def reporte_ingresos_mensual(mes, anio):
    """
    Genera un reporte mensual de ingresos totales.
    """
    ingresos_totales = 0

    for pago in pagos.pagos:
        # Aquí podríamos implementar un filtro por mes y año si tuviéramos fecha en los pagos
        ingresos_totales += pago["monto"]

    print(f"Ingresos totales en {mes}/{anio}: ${ingresos_totales}")

def reporte_horas_trabajadas_mensual(mes, anio):
    """
    Genera un reporte mensual de horas trabajadas.
    """
    horas_trabajadas = 0

    for cita in registro_citas.citas:
        # Asumimos que cada cita dura 1 hora por simplicidad
        # Aquí podríamos implementar un filtro por mes y año si tuviéramos fecha en las citas
        horas_trabajadas += 1

    print(f"Horas trabajadas en {mes}/{anio}: {horas_trabajadas} horas")

def reporte_horas_sin_cita_mensual(mes, anio, horas_disponibles):
    """
    Genera un reporte mensual de horas sin citas.
    """
    horas_trabajadas = 0

    for cita in registro_citas.citas:
        horas_trabajadas += 1

    horas_sin_cita = horas_disponibles - horas_trabajadas
    print(f"Horas sin cita en {mes}/{anio}: {horas_sin_cita} horas")


