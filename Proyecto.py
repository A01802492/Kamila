#Agenda de Control de Pacientes, expedientes y control de pagos
#Alexandra Romo

import registro_pacientes
import tratamientos_precios
import pagos
import historia_clinica
import reportes
import registro_citas

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

def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            opp1 = input("[1]Registrar un paciente\n[2]Ver lista de pacientes\nQué desea realizar?: ")
            if opp1 == "1":
                # Registro de Pacientes
                nombre = input("Ingrese el nombre del paciente: ")
                edad = input("Ingrese la edad del paciente: ")
                direccion = input("Ingrese la dirección del paciente: ")
                if edad.isdigit():
                    registro_pacientes.registrar_paciente(nombre, int(edad), direccion)
                else:
                    print("Edad no válida. Debe ser un número entero positivo.")
            else:
                # Ver Pacientes Registrados
                registro_pacientes.mostrar_pacientes()

        elif opcion == "2":
            opp2 = input("[1]Registrar una cita\n[2]Ver lista de citas\nQué desea realizar?: ")
            if opp2 == "1":
                # Ver Pacientes Registrados antes de registrar una cita
                registro_pacientes.mostrar_pacientes()

                # Registro de Citas
                paciente = input("Ingrese el nombre del paciente (debe estar registrado): ")
                fecha = input("Ingrese la fecha de la cita (AAAA-MM-DD): ")
                hora = input("Ingrese la hora de la cita (HH:MM): ")
                motivo = input("Ingrese el motivo de la cita: ")
                # Validar si el paciente está registrado
                paciente_encontrado = any(p["nombre"] == paciente for p in registro_pacientes.pacientes)
                if not paciente_encontrado:
                    print("Error: El paciente no está registrado. No se puede agendar la cita.")
                else:
                    registro_citas.agregar_cita(paciente, fecha, hora, motivo)
            else:
                registro_citas.mostrar_citas()

        elif opcion == "3":
            # Tratamientos y Precios
            nombre = input("Ingrese el nombre del tratamiento: ")
            precio = input("Ingrese el precio del tratamiento: ")
            if precio.replace('.', '', 1).isdigit():
                tratamientos_precios.registrar_tratamiento(nombre, float(precio))
            else:
                print("Precio no válido. Debe ser un número positivo.")

        elif opcion == "4":
            # Pagos
            paciente = input("Ingrese el nombre del paciente: ")
            monto = input("Ingrese el monto a pagar: ")
            if monto.replace('.', '', 1).isdigit():
                pagos.registrar_pago(paciente, float(monto))
            else:
                print("Monto no válido. Debe ser un número positivo.")

        elif opcion == "5":
            # Historia Clínica
            paciente = input("Ingrese el nombre del paciente: ")
            diagnostico = input("Ingrese el diagnóstico: ")
            tratamiento = input("Ingrese el tratamiento: ")
            observaciones = input("Ingrese las observaciones: ")
            historia_clinica.agregar_historia_clinica(paciente, diagnostico, tratamiento, observaciones)

        elif opcion == "6":
            # Reportes
            mes = input("Ingrese el mes (1-12): ")
            anio = input("Ingrese el año (AAAA): ")
            if mes.isdigit() and anio.isdigit():
                mes = int(mes)
                anio = int(anio)
                reportes.reporte_ingresos_mensual(mes, anio)
                reportes.reporte_horas_trabajadas_mensual(mes, anio)
                horas_disponibles = input("Ingrese las horas disponibles en el mes: ")
                if horas_disponibles.isdigit():
                    reportes.reporte_horas_sin_cita_mensual(mes, anio, int(horas_disponibles))
            else:
                print("Mes o año no válido.")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
