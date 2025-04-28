import re,funciones.imprimir, funciones.creacion, funciones.modificar, funciones.eliminar, funciones.conversionmatriz


# ===== MENÚ PRINCIPAL =====

def menu_principal():
    alumnos = [["1200001", "Juan", "Pérez", 32123456, "juan.perez@gmail.com"],
            ["1200002", "María", "Gómez", 33456789, "maria.gomez@yahoo.com"],
            ["1200003", "Lucas", "Fernández", 31222333, "lucas.fernandez@hotmail.com"],
            ["1200004", "Ana", "López", 34566777, "ana.lopez@gmail.com"]]

    evaluaciones = [[1, "15/03/2025", "1200001", "1204565", "Parcial", "Matemática I", 8],
                    [2, "20/04/2025", "1200304", "1201243", "Final", "Programación", 9],
                    [3, "10/05/2025", "1203854", "1204124", "Parcial", "Historia", 7],
                    [4, "05/06/2025", "1204895", "1204729", "Final", "Biología", 6]]

    profesores = {"Legajo": [1001, 1002, 1003, 1004],
                "NombreProfesores": ["Carlos", "Patricia", "Roberto", "Lucía"],
                "ApellidoProfesores": ["Martínez", "Sosa", "Alvarez", "Diaz"],
                "DNI": [22333444, 23444555, 24555666, 25666777],
                "Mail": ["carlos.martinez@universidad.edu", "patricia.sosa@universidad.edu",
                        "roberto.alvarez@universidad.edu", "lucia.diaz@universidad.edu"]}

    bandera = True
    while bandera:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ver datos\n2. Agregar\n3. Modificar\n4. Eliminar\n5. Salir")
        op = input("Opción: ")
        if op == '1':
            subMenuImprimir(alumnos,evaluaciones,profesores)
        elif op == '2':
            alumnos,evaluaciones,profesores = subMenuCreacion(alumnos,evaluaciones,profesores)
        elif op == '3':
            alumnos,evaluaciones,profesores = subMenuModificar(alumnos,evaluaciones,profesores)
        elif op == '4':
            alumnos,evaluaciones,profesores = subMenuEliminar(alumnos,evaluaciones,profesores)
        elif op == '5':
            print("¡Gracias por usar el sistema!")
            bandera = False
        else:
            print("Opción inválida.")


# ===== SUBMENÚS =====
# 
#    
def subMenuImprimir(alumnos,evaluaciones,profesores):
    bandera = True
    while bandera:
        print("Que desea ver? ")
        print("\n1. Alumnos\n2. Evaluaciones\n3. Profesores\n4. Volver")
        op = input("Opción: ")
        if op == '1':
            if type(alumnos) == 'dict':
                funciones.imprimir.imprimirMatrizDiccAlumnos(alumnos)
            else:
                funciones.imprimir.imprimirMatrizAlumnos(alumnos)
        elif op == '2':
            funciones.imprimir.imprimirMatrizEv(evaluaciones)
        elif op == '3':
            funciones.imprimir.imprimirDiccionarios(profesores)
        elif op == '4':
            bandera = False
        else:
            print("Opción inválida.")

#SUBMENÚ AGREGAR
def subMenuCreacion(alumnos,evaluaciones,profesores):
    bandera = True
    while bandera:
        print("\n1. Alumnos\n2. Evaluaciones\n3. Profesores\n4. Volver")
        op = input("Opción: ")
        if op == '1':
            matrizAlum = funciones.creacion.crearMatrizAlumnos(alumnos)
            diccAlumnos = funciones.conversionmatriz.conversionMatrizADiccioario(matrizAlum)
            funciones.imprimir.imprimirMatrizAlumnos(diccAlumnos)
        elif op == '2':
            evaluaciones = funciones.creacion.crearMatrizEvaluaciones(evaluaciones)
            funciones.imprimir.imprimirMatrizEv(evaluaciones)
        elif op == '3':
            profesores = funciones.creacion.crearDiccionarioProfesores(profesores)
            funciones.imprimir.imprimirDiccionarios(profesores)
        elif op == '4':
            bandera = False
        else:
            print("Opción inválida.")
    return alumnos,evaluaciones,profesores

#SUBMENÚ MODIFICAR
def subMenuModificar(alumnos,evaluaciones,profesores):
    bandera = True
    while bandera:
        print("\n1. Alumnos\n2. Evaluaciones\n3. Profesores\n4. Volver")
        op = input("Opción: ")
        if op == '1':
            alumnos = funciones.conversionmatriz.conversionMatrizADiccioario(alumnos)
            funciones.modificar.modificarAlumnos(alumnos)
        elif op == '2':
            evaluaciones = funciones.modificar.modificarEvaluaciones(evaluaciones)
            # Imprimir la matriz como tabla con tabulaciones
            print("\nMatriz de datos (ID | Fecha | Legajo del Alumno | Legajo del Profesor | Instancia | Materia | Calificación):\n")
    
            print("ID".ljust(20),"Fecha".ljust(20),"Legajo del Alumno".ljust(20),"Legajo del Profesor".ljust(20),"Instancia".ljust(20),"Materia","Calificación")
            print("-" * 150)

            for fila in evaluaciones:
                fecha_str = f"{fila[1][0]:02}/{fila[1][1]:02}/{fila[1][2]}"
                print(str(fila[0]).ljust(20),fecha_str.ljust(20),str(fila[2]).ljust(20),str(fila[3]).ljust(20), fila[4].ljust(20), fila[5].ljust(20), str(fila[6]).ljust(20))
    
        elif op == '3':
            profesores = funciones.modificar.modificarProfesores(profesores)
            funciones.imprimir.imprimirDiccionarios(profesores)
        elif op == '4':
            bandera = False
        else:
            print("Opción inválida.")
    return alumnos,evaluaciones,profesores    


#SUBMENÚ ELIMINAR
def subMenuEliminar(alumnos,evaluaciones,profesores):
    alumnos,evaluaciones,profesores = funciones.eliminar.eliminarElementoMenu(alumnos,evaluaciones,profesores)


menu_principal()