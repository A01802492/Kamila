def reporte_horas_sin_cita_anual(anio, horas_mensuales):
    """Genera reporte anual de horas sin cita"""
    from registro_citas import citas
    
    print(f"\nREPORTE ANUAL DE HORAS SIN CITA - {anio}")
    print("-" * 70)
    print(f"{'Mes':<15}{'Horas Disp.':<15}{'Horas Trab.':<15}{'Horas Libres':<15}{'Ocupación %':<15}")
    print("-" * 70)
    
    total_horas_trabajadas = 0
    total_horas_disponibles = 0
    
    for mes in range(1, 13):
        citas_mes = filtrar_por_mes_anio(citas, 'fecha', mes, anio)
        horas_trabajadas = len(citas_mes)
        horas_disponibles = horas_mensuales
        horas_libres = horas_disponibles - horas_trabajadas
        porcentaje = (horas_trabajadas/horas_disponibles)*100 if horas_disponibles > 0 else 0
        
        print(f"{mes:02d}/{anio:<13}{horas_disponibles:<15}{horas_trabajadas:<15}"
              f"{horas_libres:<15}{porcentaje:.2f}%")
        
        total_horas_trabajadas += horas_trabajadas
        total_horas_disponibles += horas_disponibles
    
    print("-" * 70)
    total_horas_libres = total_horas_disponibles - total_horas_trabajadas
    total_porcentaje = (total_horas_trabajadas/total_horas_disponibles)*100 if total_horas_disponibles > 0 else 0
    
    print(f"{'TOTAL':<15}{total_horas_disponibles:<15}{total_horas_trabajadas:<15}"
          f"{total_horas_libres:<15}{total_porcentaje:.2f}%")

def exportar_reporte_csv(nombre_archivo, datos, campos):
    """Exporta datos a un archivo CSV"""
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(datos)
        print(f"\nReporte exportado correctamente a {nombre_archivo}")
    except Exception as e:
        print(f"\nError al exportar el reporte: {str(e)}")

def menu_reportes():
    """Muestra el menú de reportes"""
    while True:
        print("\nMENÚ DE REPORTES")
        print("1. Reporte de ingresos mensual")
        print("2. Reporte de horas trabajadas mensual")
        print("3. Reporte de horas sin cita mensual")
        print("4. Reporte anual de horas sin cita")
        print("5. Exportar datos a CSV")
        print("6. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            mes = int(input("Ingrese el mes (1-12): "))
            anio = int(input("Ingrese el año: "))
            reporte_ingresos_mensual(mes, anio)
        
        elif opcion == "2":
            mes = int(input("Ingrese el mes (1-12): "))
            anio = int(input("Ingrese el año: "))
            reporte_horas_trabajadas_mensual(mes, anio)
        
        elif opcion == "3":
            mes = int(input("Ingrese el mes (1-12): "))
            anio = int(input("Ingrese el año: "))
            horas_disponibles = int(input("Ingrese horas disponibles en el mes: "))
            reporte_horas_sin_cita_mensual(mes, anio, horas_disponibles)
        
        elif opcion == "4":
            anio = int(input("Ingrese el año: "))
            horas_mensuales = int(input("Ingrese horas disponibles por mes: "))
            reporte_horas_sin_cita_anual(anio, horas_mensuales)
        
        elif opcion == "5":
            nombre_archivo = input("Ingrese nombre del archivo CSV (ej: reporte.csv): ")
            
            # Seleccionar qué datos exportar
            print("\nSeleccione datos a exportar:")
            print("1. Pacientes")
            print("2. Citas")
            print("3. Pagos")
            tipo_datos = input("Opción: ")
            
            if tipo_datos == "1":
                from main import pacientes
                campos = ['nombre', 'edad', 'direccion', 'fecha_registro']
                exportar_reporte_csv(nombre_archivo, pacientes, campos)
            elif tipo_datos == "2":
                from registro_citas import citas
                campos = ['fecha', 'hora', 'paciente', 'motivo', 'estado']
                exportar_reporte_csv(nombre_archivo, citas, campos)
            elif tipo_datos == "3":
                from pagos import pagos
                campos = ['fecha', 'paciente', 'monto', 'metodo_pago']
                exportar_reporte_csv(nombre_archivo, pagos, campos)
            else:
                print("Opción no válida")
        
        elif opcion == "6":
            break
        
        else:
            print("Opción no válida, intente nuevamente")