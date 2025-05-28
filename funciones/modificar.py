#La idea sería acceder a la columna que se desea modificar atraves de su indice y compararlo con un if anidado
#Y a su vez con algún método comparar la posición del dato a buscar, y acceder a la matriz con este indice y con la posicion del if

#matrizAlumnos = creacion.CrearMatrizAlumnos()
#alumnosDiccionario = conversionmatriz.conversionMatrizADiccioario(matrizAlumnos)
#matrizEvaluaciones = creacion.CrearMatrizEvaluaciones()
#diccionarioProfesores = creacion.crearDiccionarioProfesores()

#Se crea la matriz de alumnos y se convierte a diccionario
#Se crea la matriz de evaluaciones
#Se crea la matriz de profesores y se convierte a diccionario
from funciones.creacion import ingresarNumeros, validarOpciones


def modificarAlumnos(alumnosDiccionario):
    opcionesValidas = [1, 2, 3, 4, 5]
    opcion = validarOpciones(opcionesValidas, "\nQué dato de la evaluación desea modificar?" \
    "\n---------------------------" \
    "\nOpción 1: Nombre" \
        "\nOpción 2: Apellido" \
            "\nOpción 3: DNI" \
                "\nOpción 4: Mail" \
                    "\nOpción 5: Salir" \
                        "\n---------------------------" \
                            "\nQue opción desea elegir?: ")

    opcion = int(opcion)

    if opcion == 5:
        print("Saliendo de la modificación de Alumnos.")
    else:
        print("\nLos legajos disponibles son: ")
        for alumno in alumnosDiccionario:
            print(f"- {alumno["Legajo"]}")

        legajoEncontrado = False
        viejoLegajo = input("Ingrese el legajo a modificar: ")
        if viejoLegajo.isdigit():
            viejoLegajo = int(viejoLegajo)
        else:
            print("El legajo ingresado no es válido, por favor vuelva a ingresar un legajo que sí lo sea")
            print("\nLos Legajos de Alumnos disponibles son: ")
            for alumno in alumnosDiccionario:
                print(f"- {alumno["Legajo"]}")
            viejoLegajo = int(input("Ingrese el legajo a modificar: "))

        for alumno in alumnosDiccionario:
            if alumno["Legajo"] == viejoLegajo:
                legajoEncontrado = True

                if opcion == 1:
                    print("El nombre actual es: ", alumno["NombreAlumno"])
                    nuevoNombre = input("Ingrese el nuevo nombre: ")
                    alumno["NombreAlumno"] = nuevoNombre
                elif opcion == 2:
                    print("El apellido actual es: ", alumno["ApellidoAlumno"])
                    nuevoApellido = input("Ingrese el nuevo apellido: ")
                    alumno["ApellidoAlumno"] = nuevoApellido
                elif opcion == 3:
                    print("El DNI actual es: ", alumno["DNI"])
                    nuevoDNI = int(input("Ingrese el nuevo DNI: "))
                    alumno["DNI"] = nuevoDNI
                elif opcion == 4:
                    print("El mail actual es: ", alumno["Mail"])
                    nuevoMail = input("Ingrese el nuevo mail: ")
                    alumno["Mail"] = nuevoMail

                print("El dato se ha modificado correctamente")
                print("\nDatos actualizados del alumno:")
                print(f"Legajo: {alumno['Legajo']}")
                print(f"Nombre: {alumno['NombreAlumno']}")
                print(f"Apellido: {alumno['ApellidoAlumno']}")
                print(f"DNI: {alumno['DNI']}")
                print(f"Mail: {alumno['Mail']}")

        if not legajoEncontrado:
            print("El legajo ingresado no se encuentra en la lista de alumnos")
            print("Por favor, vuelva a ingresar un legajo que sí esté en la lista")
            print("\nLos legajos disponibles son: ")
            for alumno in alumnosDiccionario:
                print(f"- {alumno['Legajo']}")

    return alumnosDiccionario

def modificarEvaluaciones(matrizEvaluaciones):
    opcionesValidas = [1, 2, 3, 4, 5, 6, 7]
    opcion = validarOpciones(opcionesValidas, "\nQué dato de la evaluación desea modificar?" \
    "\n---------------------------" \
    "\nOpción 1: Fecha" \
        "\nOpción 2: Legajo del Alumno" \
            "\nOpción 3: Legajo del Profesor" \
                "\nOpción 4: Instancia" \
                    "\nOpción 5: Materia" \
                        "\nOpción 6: Calificación" \
                            "\nOpción 7: Salir" \
                                "\n---------------------------" \
                                    "\nQue opción desea elegir?: ")
    int(opcion)
    #Validación de la opción 

    if opcion == 7:
        print("Saliendo de la modificación de Evaluaciones.")
    else:
        print("\nIDs de las evaluaciones disponibles: ")
        for evaluacion in matrizEvaluaciones:
            print(f"- {evaluacion[0]}")
            #Muestra el id de cada evaluación

        idBuscar = input("Ingrese el ID de la evaluación a modificar: ")

        while not idBuscar.isdigit():
            print("El ID ingresado no es válido, por favor vuelva a ingresar un ID que sí lo sea")
            print("\nIDs de las evaluaciones disponibles: ")
            for evaluacion in matrizEvaluaciones:
                print(f"- {evaluacion[0]}")
                #Muestra el id de cada evaluación
            idBuscar = input("Ingrese el ID de la evaluación a modificar: ")

        idBuscar = int(idBuscar)

        idEncontrado = False
        for evaluacion in matrizEvaluaciones:
            if evaluacion[0] == idBuscar:
                idEncontrado = True

                if opcion == 1:
                    print("La fecha actual es: ", evaluacion[1])
                    print("Formato de fecha: dd/mm/aaaa")
                    dia = int(input("Ingrese el nuevo día: "))
                    mes = int(input("Ingrese el nuevo mes: "))
                    anio = int(input("Ingrese el nuevo año: "))
                    nuevaFecha = (dia, mes, anio)
                    evaluacion[1] = dia
                    evaluacion[2] = mes
                    evaluacion[3] = anio
                elif opcion == 2:
                    print("El legajo del alumno actual es: ", evaluacion[4])
                    nuevoLegajoAlumno = int(input("Ingrese el nuevo legajo del alumno: "))
                    evaluacion[4] = nuevoLegajoAlumno
                elif opcion == 3:
                    print("El legajo del profesor actual es: ", evaluacion[5])
                    nuevoLegajoProfesor = int(input("Ingrese el nuevo legajo del profesor: "))
                    evaluacion[5] = nuevoLegajoProfesor
                elif opcion == 4:
                    print("La instancia evaluativa actual es: ", evaluacion[6])
                    nuevaInstancia = input("Ingrese la nueva instancia evaluativa: ")
                    evaluacion[6] = nuevaInstancia
                elif opcion == 5:
                    print("La materia actual es: ", evaluacion[7])
                    nuevaMateria = input("Ingrese la nueva materia: ")
                    evaluacion[7] = nuevaMateria
                elif opcion == 6:
                    print("La calificación actual es: ", evaluacion[8])
                    nuevaCalificacion = float(input("Ingrese la nueva calificación: "))
                    evaluacion[8] = nuevaCalificacion

                print("El dato se ha modificado correctamente")
                
        if not idEncontrado:
            print("El ID ingresado no se encuentra en la lista de evaluaciones")
            print("Por favor, vuelva a ingresar un ID que sí esté en la lista")
            print("\nIDs de las evaluaciones disponibles: ")
            for evaluacion in matrizEvaluaciones:
                print(f"- {evaluacion[0]}")

    return matrizEvaluaciones


def modificarProfesores(profesores):
    opcionesValidas = [1, 2, 3, 4, 5]
    opcion = validarOpciones(opcionesValidas, "\nQué dato del profesor desea modificar?" \
    "\n---------------------------" \
    "\nOpción 1: Nombre" \
        "\nOpción 2: Apellido" \
            "\nOpción 3: DNI" \
                "\nOpción 4: Mail" \
                    "\nOpción 5: Salir" \
                        "\n---------------------------" \
                        "\nQue opción desea elegir?: ")
    int(opcion)
    
    if opcion == 5:
        print("Saliendo de la modificación de profesores.")
    else:
        print("\nLos legajos disponibles son: ")
        for profesor in profesores:
            print(f"- {profesor['Legajo']}")

        legajoEncontrado = False
        viejoLegajo = input("Ingrese el legajo a modificar: ")
        if viejoLegajo.isdigit():
            viejoLegajo = int(viejoLegajo)
        else:
            print("El legajo ingresado no es válido, por favor vuelva a ingresar un legajo que sí lo sea")
            print("\nLos Legajos de Profesores disponibles son: ")
            for profesor in profesores:
                print(f"- {profesor['Legajo']}")
            viejoLegajo = int(input("Ingrese el legajo a modificar: "))

        for profesor in profesores:
            if profesor["Legajo"] == viejoLegajo:
                legajoEncontrado = True

                if opcion == 1:
                    print("El nombre actual es: ", profesor["Nombre"])
                    nuevoNombre = input("Ingrese el nuevo nombre: ")
                    profesor["Nombre"] = nuevoNombre
                elif opcion == 2:
                    print("El apellido actual es: ", profesor["Apellido"])
                    nuevoApellido = input("Ingrese el nuevo apellido: ")
                    profesor["Apellido"] = nuevoApellido
                elif opcion == 3:
                    print("El DNI actual es: ", profesor["DNI"])
                    nuevoDNI = int(input("Ingrese el nuevo DNI: "))
                    profesor["DNI"] = nuevoDNI
                elif opcion == 4:
                    print("El mail actual es: ", profesor["Mail"])
                    nuevoMail = input("Ingrese el nuevo mail: ")
                    profesor["Mail"] = nuevoMail

                print("El dato se ha modificado correctamente")
                print("\nDatos actualizados del profesor:")
                print(f"Legajo: {profesor['Legajo']}")
                print(f"Nombre: {profesor['Nombre']}")
                print(f"Apellido: {profesor['Apellido']}")
                print(f"DNI: {profesor['DNI']}")
                print(f"Mail: {profesor['Mail']}")

        if not legajoEncontrado:
            print("El legajo ingresado no se encuentra en la lista de profesores")
            print("Por favor, vuelva a ingresar un legajo que sí esté en la lista")
            print("\nLos legajos disponibles son: ")
            for profesor in profesores:
                print(f"- {profesor['Legajo']}")

    return profesores

