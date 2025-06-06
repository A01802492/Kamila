# Agenda de Control de Pacientes, expedientes y control de pagos
# Alexandra Romo - Versión Mejorada

import registro_pacientes
import tratamientos_precios
import pagos
import historia_clinica
import reportes
import registro_citas
import pickle
import os
from datetime import datetime

def guardar_datos():
    """Guarda todos los datos en archivos"""
    datos = {
        'pacientes': registro_pacientes.pacientes,
        'citas': registro_citas.citas,
        'tratamientos': tratamientos_precios.tratamientos,
        'pagos': pagos.pagos,
        'historias': historia_clinica.historias_clinicas
    }
    with open('datos_consultorio.dat', 'wb') as f:
        pickle.dump(datos, f)

def cargar_datos():
    """Carga los datos desde archivos"""
    try:
        with open('datos_consultorio.dat', 'rb') as f:
            datos = pickle.load(f)
            registro_pacientes.pacientes = datos.get('pacientes', [])
            registro_citas.citas = datos.get('citas', [])
            tratamientos_precios.tratamientos = datos.get('tratamientos', [])
            pagos.pagos = datos.get('pagos', [])
            historia_clinica.historias_clinica = datos.get('historias', [])
    except (FileNotFoundError, EOFError):
        pass  # Primera ejecución, no hay datos

def mostrar_menu_principal():
    print("\n--- Agenda de Control de Pacientes ---")
    print("1. Registro de Pacientes")
    print("2. Registro de Citas")
    print("3. Tratamientos y Precios")
    print("4. Pagos")
    print("5. Historia Clínica")
    print("6. Reportes")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion

def menu_pacientes():
    while True:
        print("\n--- Gestión de Pacientes ---")
        print("1. Registrar nuevo paciente")
        print("2. Ver lista de pacientes")
        print("3. Modificar paciente")
        print("4. Eliminar paciente")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            edad = input("Edad del paciente: ")
            direccion = input("Dirección del paciente: ")
            
            if not edad.isdigit() or int(edad) <= 0:
                print("Error: Edad no válida")
                continue
                
            if registro_pacientes.existe_paciente(nombre):
                print("Error: Ya existe un paciente con ese nombre")
                continue
                
            registro_pacientes.registrar_paciente(nombre, int(edad), direccion)
            print("Paciente registrado exitosamente!")
            
        elif opcion == "2":
            registro_pacientes.mostrar_pacientes()
            
        elif opcion == "3":
            registro_pacientes.mostrar_pacientes()
            if registro_pacientes.pacientes:
                try:
                    idx = int(input("Índice del paciente a modificar: "))
                    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    nueva_edad = input("Nueva edad (dejar vacío para no cambiar): ")
                    nueva_dir = input("Nueva dirección (dejar vacío para no cambiar): ")
                    
                    registro_pacientes.modificar_paciente(
                        idx,
                        nuevo_nombre if nuevo_nombre else None,
                        int(nueva_edad) if nueva_edad else None,
                        nueva_dir if nueva_dir else None
                    )
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "4":
            registro_pacientes.mostrar_pacientes()
            if registro_pacientes.pacientes:
                try:
                    idx = int(input("Índice del paciente a eliminar: "))
                    registro_pacientes.eliminar_paciente(idx)
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida")

def menu_citas():
    while True:
        print("\n--- Gestión de Citas ---")
        print("1. Registrar nueva cita")
        print("2. Ver lista de citas")
        print("3. Modificar cita")
        print("4. Cancelar cita")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registro_pacientes.mostrar_pacientes()
            if not registro_pacientes.pacientes:
                continue
                
            paciente = input("Nombre del paciente: ")
            if not registro_pacientes.existe_paciente(paciente):
                print("Error: Paciente no registrado")
                continue
                
            fecha = input("Fecha (AAAA-MM-DD): ")
            hora = input("Hora (HH:MM): ")
            motivo = input("Motivo de la cita: ")
            
            # Verificar conflicto de horario
            if registro_citas.existe_cita(fecha, hora):
                print("Error: Ya existe una cita en ese horario")
                continue
                
            registro_citas.agregar_cita(paciente, fecha, hora, motivo)
            print("Cita registrada exitosamente!")
            
        elif opcion == "2":
            registro_citas.mostrar_citas()
            
        elif opcion == "3":
            registro_citas.mostrar_citas()
            if registro_citas.citas:
                try:
                    idx = int(input("Índice de la cita a modificar: "))
                    nueva_fecha = input("Nueva fecha (dejar vacío para no cambiar): ")
                    nueva_hora = input("Nueva hora (dejar vacío para no cambiar): ")
                    nuevo_motivo = input("Nuevo motivo (dejar vacío para no cambiar): ")
                    
                    registro_citas.modificar_cita(
                        idx,
                        nueva_fecha if nueva_fecha else None,
                        nueva_hora if nueva_hora else None,
                        nuevo_motivo if nuevo_motivo else None
                    )
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "4":
            registro_citas.mostrar_citas()
            if registro_citas.citas:
                try:
                    idx = int(input("Índice de la cita a cancelar: "))
                    registro_citas.cancelar_cita(idx)
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida")

def menu_tratamientos():
    while True:
        print("\n--- Gestión de Tratamientos ---")
        print("1. Registrar nuevo tratamiento")
        print("2. Ver lista de tratamientos")
        print("3. Modificar tratamiento")
        print("4. Eliminar tratamiento")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del tratamiento: ")
            precio = input("Precio del tratamiento: ")
            
            try:
                precio = float(precio)
                if precio <= 0:
                    raise ValueError
            except ValueError:
                print("Error: Precio no válido")
                continue
                
            tratamientos_precios.registrar_tratamiento(nombre, precio)
            print("Tratamiento registrado exitosamente!")
            
        elif opcion == "2":
            tratamientos_precios.mostrar_tratamientos()
            
        elif opcion == "3":
            tratamientos_precios.mostrar_tratamientos()
            if tratamientos_precios.tratamientos:
                try:
                    idx = int(input("Índice del tratamiento a modificar: "))
                    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ")
                    
                    if nuevo_precio:
                        try:
                            nuevo_precio = float(nuevo_precio)
                            if nuevo_precio <= 0:
                                raise ValueError
                        except ValueError:
                            print("Error: Precio no válido")
                            continue
                            
                    tratamientos_precios.modificar_tratamiento(
                        idx,
                        nuevo_nombre if nuevo_nombre else None,
                        float(nuevo_precio) if nuevo_precio else None
                    )
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "4":
            tratamientos_precios.mostrar_tratamientos()
            if tratamientos_precios.tratamientos:
                try:
                    idx = int(input("Índice del tratamiento a eliminar: "))
                    tratamientos_precios.eliminar_tratamiento(idx)
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida")

def menu_pagos():
    while True:
        print("\n--- Gestión de Pagos ---")
        print("1. Registrar nuevo pago")
        print("2. Ver lista de pagos")
        print("3. Modificar pago")
        print("4. Eliminar pago")
        print("5. Ver pagos pendientes")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registro_pacientes.mostrar_pacientes()
            if not registro_pacientes.pacientes:
                continue
                
            paciente = input("Nombre del paciente: ")
            if not registro_pacientes.existe_paciente(paciente):
                print("Error: Paciente no registrado")
                continue
                
            tratamientos_precios.mostrar_tratamientos()
            if not tratamientos_precios.tratamientos:
                continue
                
            tratamiento = input("Nombre del tratamiento: ")
            if not tratamientos_precios.existe_tratamiento(tratamiento):
                print("Error: Tratamiento no registrado")
                continue
                
            monto = input("Monto pagado: ")
            fecha = input("Fecha del pago (AAAA-MM-DD): ")
            
            try:
                monto = float(monto)
                if monto <= 0:
                    raise ValueError
            except ValueError:
                print("Error: Monto no válido")
                continue
                
            if not registro_citas.validar_fecha(fecha):
                print("Error: Fecha no válida")
                continue
                
            pagos.registrar_pago(paciente, tratamiento, monto, fecha)
            print("Pago registrado exitosamente!")
            
        elif opcion == "2":
            pagos.mostrar_pagos()
            
        elif opcion == "3":
            pagos.mostrar_pagos()
            if pagos.pagos:
                try:
                    idx = int(input("Índice del pago a modificar: "))
                    nuevo_monto = input("Nuevo monto (dejar vacío para no cambiar): ")
                    nueva_fecha = input("Nueva fecha (dejar vacío para no cambiar): ")
                    
                    if nuevo_monto:
                        try:
                            nuevo_monto = float(nuevo_monto)
                            if nuevo_monto <= 0:
                                raise ValueError
                        except ValueError:
                            print("Error: Monto no válido")
                            continue
                            
                    pagos.modificar_pago(
                        idx,
                        float(nuevo_monto) if nuevo_monto else None,
                        nueva_fecha if nueva_fecha else None
                    )
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "4":
            pagos.mostrar_pagos()
            if pagos.pagos:
                try:
                    idx = int(input("Índice del pago a eliminar: "))
                    pagos.eliminar_pago(idx)
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "5":
            pagos.mostrar_pagos_pendientes()
            
        elif opcion == "6":
            break
            
        else:
            print("Opción no válida")

def menu_historia_clinica():
    while True:
        print("\n--- Historia Clínica ---")
        print("1. Agregar registro")
        print("2. Ver historias clínicas")
        print("3. Modificar registro")
        print("4. Eliminar registro")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registro_pacientes.mostrar_pacientes()
            if not registro_pacientes.pacientes:
                continue
                
            paciente = input("Nombre del paciente: ")
            if not registro_pacientes.existe_paciente(paciente):
                print("Error: Paciente no registrado")
                continue
                
            diagnostico = input("Diagnóstico: ")
            tratamiento = input("Tratamiento aplicado: ")
            observaciones = input("Observaciones: ")
            fecha = input("Fecha (AAAA-MM-DD): ")
            
            if not registro_citas.validar_fecha(fecha):
                print("Error: Fecha no válida")
                continue
                
            historia_clinica.agregar_historia_clinica(
                paciente, diagnostico, tratamiento, observaciones, fecha
            )
            print("Registro agregado exitosamente!")
            
        elif opcion == "2":
            historia_clinica.mostrar_historias_clinicas()
            
        elif opcion == "3":
            historia_clinica.mostrar_historias_clinicas()
            if historia_clinica.historias_clinicas:
                try:
                    idx = int(input("Índice del registro a modificar: "))
                    nuevo_diag = input("Nuevo diagnóstico (dejar vacío para no cambiar): ")
                    nuevo_trat = input("Nuevo tratamiento (dejar vacío para no cambiar): ")
                    nuevas_obs = input("Nuevas observaciones (dejar vacío para no cambiar): ")
                    nueva_fecha = input("Nueva fecha (dejar vacío para no cambiar): ")
                    
                    historia_clinica.modificar_historia_clinica(
                        idx,
                        nuevo_diag if nuevo_diag else None,
                        nuevo_trat if nuevo_trat else None,
                        nuevas_obs if nuevas_obs else None,
                        nueva_fecha if nueva_fecha else None
                    )
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "4":
            historia_clinica.mostrar_historias_clinicas()
            if historia_clinica.historias_clinicas:
                try:
                    idx = int(input("Índice del registro a eliminar: "))
                    historia_clinica.eliminar_historia_clinica(idx)
                except (ValueError, IndexError):
                    print("Error: Índice no válido")
                    
        elif opcion == "5":
            break
            
        else:
            print("Opción no válida")

def menu_reportes():
    while True:
        print("\n--- Reportes ---")
        print("1. Reporte mensual de ingresos")
        print("2. Reporte mensual de horas trabajadas")
        print("3. Reporte mensual de horas sin cita")
        print("4. Reporte anual de horas sin cita")
        print("5. Exportar datos a CSV")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mes = input("Mes (1-12): ")
            anio = input("Año (AAAA): ")
            
            try:
                mes = int(mes)
                anio = int(anio)
                if mes < 1 or mes > 12:
                    raise ValueError
            except ValueError:
                print("Error: Mes o año no válidos")
                continue
                
            reportes.reporte_ingresos_mensual(mes, anio)
            
        elif opcion == "2":
            mes = input("Mes (1-12): ")
            anio = input("Año (AAAA): ")
            
            try:
                mes = int(mes)
                anio = int(anio)
                if mes < 1 or mes > 12:
                    raise ValueError
            except ValueError:
                print("Error: Mes o año no válidos")
                continue
                
            reportes.reporte_horas_trabajadas_mensual(mes, anio)
            
        elif opcion == "3":
            mes = input("Mes (1-12): ")
            anio = input("Año (AAAA): ")
            horas = input("Horas disponibles en el mes: ")
            
            try:
                mes = int(mes)
                anio = int(anio)
                horas = int(horas)
                if mes < 1 or mes > 12 or horas <= 0:
                    raise ValueError
            except ValueError:
                print("Error: Datos no válidos")
                continue
                
            reportes.reporte_horas_sin_cita_mensual(mes, anio, horas)
            
        elif opcion == "4":
            anio = input("Año (AAAA): ")
            horas = input("Horas disponibles por mes: ")
            
            try:
                anio = int(anio)
                horas = int(horas)
                if horas <= 0:
                    raise ValueError
            except ValueError:
                print("Error: Datos no válidos")
                continue
                
            reportes.reporte_horas_sin_cita_anual(anio, horas)
            
        elif opcion == "5":
            print("\nExportar datos a CSV:")
            print("1. Pacientes")
            print("2. Citas")
            print("3. Tratamientos")
            print("4. Pagos")
            print("5. Historias clínicas")
            print("6. Cancelar")
            
            op = input("Seleccione qué datos exportar: ")
            
            if op == "1":
                reportes.exportar_a_csv(registro_pacientes.pacientes, "pacientes.csv")
            elif op == "2":
                reportes.exportar_a_csv(registro_citas.citas, "citas.csv")
            elif op == "3":
                reportes.exportar_a_csv(tratamientos_precios.tratamientos, "tratamientos.csv")
            elif op == "4":
                reportes.exportar_a_csv(pagos.pagos, "pagos.csv")
            elif op == "5":
                reportes.exportar_a_csv(historia_clinica.historias_clinicas, "historias_clinicas.csv")
            elif op == "6":
                pass
            else:
                print("Opción no válida")
                
        elif opcion == "6":
            break
            
        else:
            print("Opción no válida")

def main():
    # Cargar datos al iniciar
    cargar_datos()
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_citas()
        elif opcion == "3":
            menu_tratamientos()
        elif opcion == "4":
            menu_pagos()
        elif opcion == "5":
            menu_historia_clinica()
        elif opcion == "6":
            menu_reportes()
        elif opcion == "7":
            # Guardar datos al salir
            guardar_datos()
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()