import funciones.imprimir, funciones.creacion, funciones.modificar, funciones.eliminar, funciones.conversionmatriz


def menu_principal():
    alumnos = [[120333, "Juan", "Pérez", 32123456, "juan.perez@gmail.com"],
            [120444, "María", "Gómez", 33456789, "maria.gomez@yahoo.com"],
            [120555, "Lucas", "Fernández", 31222333, "lucas.fernandez@hotmail.com"],
            [120222, "Ana", "López", 34566777, "ana.lopez@gmail.com"]]

    evaluaciones = [[1, "15","03","2025", "1200001", "1204565", "Parcial", "Matemática I", 8],
                    [2, "20","04","2025", "1200304", "1201243", "Final", "Programación", 9],
                    [3, "10","05","2025", "1203854", "1204124", "Parcial", "Historia", 7],
                    [4, "05","06","2025", "1204895", "1204729", "Final", "Biología", 6]]

    profesores = {"Legajo": [1001, 1002, 1003, 1004],
                "NombreProfesores": ["Carlos", "Patricia", "Roberto", "Lucía"],
                "ApellidoProfesores": ["Martínez", "Sosa", "Alvarez", "Diaz"],
                "DNI": [22333444, 23444555, 24555666, 25666777],
                "Mail": ["carlos.martinez@universidad.edu", "patricia.sosa@universidad.edu",
                        "roberto.alvarez@universidad.edu", "lucia.diaz@universidad.edu"]}

    bandera = True
    while bandera:
        print("\n===== MENÚ PRINCIPAL =====")
        print("Seleccione la entidad:")
        print("1. Alumnos\n2. Evaluaciones\n3. Profesores\n4. Salir")
        entidad = input("Opción: ")

        if entidad == '4':
            print("¡Gracias por usar el sistema!")
            bandera = False
        elif entidad == '1' or entidad == '2' or entidad == '3':
            print("\nSeleccione la operación:")
            print("1. Ver\n2. Agregar\n3. Modificar\n4. Eliminar\n5. Volver")
            operacion = input("Opción: ")

            if operacion == '1':
                subMenuImprimir(alumnos, evaluaciones, profesores, entidad)
            elif operacion == '2':
                alumnos, evaluaciones, profesores = subMenuCreacion(alumnos, evaluaciones, profesores, entidad)
            elif operacion == '3':
                alumnos, evaluaciones, profesores = subMenuModificar(alumnos, evaluaciones, profesores, entidad)
            elif operacion == '4':
                alumnos, evaluaciones, profesores = subMenuEliminar(alumnos, evaluaciones, profesores, entidad)
            elif operacion == '5':
                continue
            else:
                print("Opción inválida.")
        else:
            print("Opción inválida.")


# ===== SUBMENÚS =====
def subMenuImprimir(alumnos, evaluaciones, profesores, entidad):
    if entidad == '1':
        if type(alumnos[0]) == list:
            funciones.imprimir.imprimirMatrizAlumnos(alumnos)
        else:
            funciones.imprimir.imprimirMatrizDiccAlumnos(alumnos)
    elif entidad == '2':
        funciones.imprimir.imprimirMatrizEv(evaluaciones)
    elif entidad == '3':
        funciones.imprimir.imprimirDiccionarios(profesores)

def subMenuCreacion(alumnos, evaluaciones, profesores, entidad):
    if entidad == '1':
        if type(alumnos[0]) == list:
            alumnos = funciones.creacion.crearMatrizAlumnos(alumnos)
            alumnos = funciones.conversionmatriz.conversionMatrizADiccioario(alumnos)
            funciones.imprimir.imprimirMatrizDiccAlumnos(alumnos)
        else:
            alumnos = funciones.conversionmatriz.convertirDiccionarioEnMatriz(alumnos)
            alumnos = funciones.creacion.crearMatrizAlumnos(alumnos)
            funciones.imprimir.imprimirMatrizAlumnos(alumnos)
            alumnos = funciones.conversionmatriz.conversionMatrizADiccioario(alumnos)
    elif entidad == '2':
        evaluaciones = funciones.creacion.CrearMatrizEvaluaciones(evaluaciones)
        funciones.imprimir.imprimirMatrizEv(evaluaciones)
    elif entidad == '3':
        profesores = funciones.creacion.crearDiccionarioProfesores(profesores)
        funciones.imprimir.imprimirDiccionarios(profesores)
    return alumnos, evaluaciones, profesores

def subMenuModificar(alumnos, evaluaciones, profesores, entidad):
    if entidad == '1':
        if type(alumnos[0]) == list:
            alumnos = funciones.conversionmatriz.conversionMatrizADiccioario(alumnos)
        alumnos = funciones.modificar.modificarAlumnos(alumnos)
        funciones.imprimir.imprimirMatrizDiccAlumnos(alumnos)
    elif entidad == '2':
        evaluaciones = funciones.modificar.modificarEvaluaciones(evaluaciones)
        funciones.imprimir.imprimirMatrizEv(evaluaciones)
    elif entidad == '3':
        profesores = funciones.modificar.modificarProfesores(profesores)
        funciones.imprimir.imprimirDiccionarios(profesores)
    return alumnos, evaluaciones, profesores

def subMenuEliminar(alumnos, evaluaciones, profesores, entidad):
    if type(alumnos[0]) == list:
        alumnos = funciones.conversionmatriz.conversionMatrizADiccioario(alumnos)
    alumnos, evaluaciones, profesores = funciones.eliminar.eliminarElementoMenu(alumnos, evaluaciones, profesores, entidad)
    return alumnos, evaluaciones, profesores


menu_principal()