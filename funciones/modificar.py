#La idea sería acceder a la columna que se desea modificar atraves de su indice y compararlo con un if anidado
#Y a su vez con algún método comparar la posición del dato a buscar, y acceder a la matriz con este indice y con la posicion del if
import creacion
import conversionmatriz

#matrizAlumnos = creacion.CrearMatrizAlumnos()
#alumnosDiccionario = conversionmatriz.conversionMatrizADiccioario(matrizAlumnos)
#matrizEvaluaciones = creacion.CrearMatrizEvaluaciones()
diccionarioProfesores = creacion.crearDiccionarioProfesores()

#Se crea la matriz de alumnos y se convierte a diccionario
#Se crea la matriz de evaluaciones
#Se crea la matriz de profesores y se convierte a diccionario


def modificarAlumnos(alumnosDiccionario):
    print("---------------------------")
    print("Opción 1: Legajo")
    print("Opción 2: Nombre")
    print("Opción 3: Apellido")
    print("Opción 4: DNI")
    print("Opción 5: Mail")
    print("---------------------------")

    opcion = input("Que opción desea elegir? ")
    # Validación de la opción
    validarOpcion = opcion.isdigit()
    while not validarOpcion:
        print("El dato ingresado no es válido, por favor vuelva a ingresar un dato que sí lo sea")
        print("---------------------------")
        print("Opción 1: Legajo")
        print("Opción 2: Nombre")
        print("Opción 3: Apellido")
        print("Opción 4: DNI")
        print("Opción 5: Mail")
        print("---------------------------")
        opcion = input("Que opción desea elegir?: ")
        validarOpcion = opcion.isdigit()

    opcion = int(opcion)
    while opcion not in range(1, 6):
        print("Número de opción no válido, por favor volver a ingresar uno que sí lo sea")
        opcion = int(input("Qué opción desea elegir?: "))

    print("\nLos legajos disponibles son: ")
    for alumno in alumnosDiccionario:
        print(f"- {alumno['Legajo']}")

    legajoEncontrado = False
    viejoLegajo = input("Ingrese el legajo a modificar: ")
    if viejoLegajo.isdigit():
        viejoLegajo = int(viejoLegajo)
    else:
        print("El legajo ingresado no es válido, por favor vuelva a ingresar un legajo que sí lo sea")
        print("\nLos Legajos de Alumnos disponibles son: ")
        for alumno in alumnosDiccionario:
            print(f"- {alumno['Legajo']}")
        viejoLegajo = int(input("Ingrese el legajo a modificar: "))

    for alumno in alumnosDiccionario:
        if alumno["Legajo"] == viejoLegajo:
            legajoEncontrado = True

            if opcion == 1:
                print("El legajo actual es: ", alumno["Legajo"])
                print("Formato de legajo: 120XXXX")
                nuevoLegajo = int(input("Ingrese el nuevo legajo: "))
                alumno["Legajo"] = nuevoLegajo
            elif opcion == 2:
                print("El nombre actual es: ", alumno["NombreAlumno"])
                nuevoNombre = input("Ingrese el nuevo nombre: ")
                alumno["NombreAlumno"] = nuevoNombre
            elif opcion == 3:
                print("El apellido actual es: ", alumno["ApellidoAlumno"])
                nuevoApellido = input("Ingrese el nuevo apellido: ")
                alumno["ApellidoAlumno"] = nuevoApellido
            elif opcion == 4:
                print("El DNI actual es: ", alumno["DNI"])
                nuevoDNI = int(input("Ingrese el nuevo DNI: "))
                alumno["DNI"] = nuevoDNI
            elif opcion == 5:
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
    print("\nQué dato de la evaluación desea modificar?")
    print("---------------------------")
    print("Opción 1: Fecha")
    print("Opción 2: Legajo del Alumno")
    print("Opción 3: Legajo del Profesor")
    print("Opción 4: Instancia Evaluativa")
    print("Opción 5: Materia")
    print("Opción 6: Calificación")
    print("---------------------------")

    opcion = input("Que opción desea elegir? ")
    #Pido la opción a modificar

    #Validación de la opción
    validarOpcion = opcion.isdigit()
    while not validarOpcion or int(opcion) not in range(1,7):

        #Validación de la opción
        print("El dato ingresado no es válido, por favor vuelva a ingresar un dato que sí lo sea")
        print("---------------------------")
        print("Opción 1: Fecha")
        print("Opción 2: Legajo del Alumno")
        print("Opción 3: Legajo del Profesor")
        print("Opción 4: Instancia Evaluativa")
        print("Opción 5: Materia")
        print("Opción 6: Calificación")
        print("---------------------------")
        opcion = input("Que opción desea elegir?: ")
        validarOpcion = opcion.isdigit()

    opcion = int(opcion)
    #Validación de la opción 


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
                evaluacion[1] = nuevaFecha
            elif opcion == 2:
                print("El legajo del alumno actual es: ", evaluacion[2])
                nuevoLegajoAlumno = int(input("Ingrese el nuevo legajo del alumno: "))
                evaluacion[2] = nuevoLegajoAlumno
            elif opcion == 3:
                print("El legajo del profesor actual es: ", evaluacion[3])
                nuevoLegajoProfesor = int(input("Ingrese el nuevo legajo del profesor: "))
                evaluacion[3] = nuevoLegajoProfesor
            elif opcion == 4:
                print("La instancia evaluativa actual es: ", evaluacion[4])
                nuevaInstancia = input("Ingrese la nueva instancia evaluativa: ")
                evaluacion[4] = nuevaInstancia
            elif opcion == 5:
                print("La materia actual es: ", evaluacion[5])
                nuevaMateria = input("Ingrese la nueva materia: ")
                evaluacion[5] = nuevaMateria
            elif opcion == 6:
                print("La calificación actual es: ", evaluacion[6])
                nuevaCalificacion = float(input("Ingrese la nueva calificación: "))
                evaluacion[6] = nuevaCalificacion

            print("El dato se ha modificado correctamente")
            print("\nDatos actualizados de la evaluación:")
            print(f"ID: {evaluacion[0]}")
            print(f"Fecha: {evaluacion[1]}")
            print(f"Legajo del Alumno: {evaluacion[2]}")
            print(f"Legajo del Profesor: {evaluacion[3]}")
            print(f"Instancia Evaluativa: {evaluacion[4]}")
            print(f"Materia: {evaluacion[5]}")
            print(f"Calificación: {evaluacion[6]}")
    if not idEncontrado:
        print("El ID ingresado no se encuentra en la lista de evaluaciones")
        print("Por favor, vuelva a ingresar un ID que sí esté en la lista")
        print("\nIDs de las evaluaciones disponibles: ")
        for evaluacion in matrizEvaluaciones:
            print(f"- {evaluacion[0]}")

    return matrizEvaluaciones



def modificarProfesores(profesores):
    bandera = True

    while bandera:
        for i in range(len(profesores["Legajo"])):
            print(f"- {profesores['Legajo'][i]}") 
        legajo = input("Ingrese legajo del profesor a modificar: ")

        # Validación de legajo
        while not legajo.isdigit() or int(legajo) not in profesores["Legajo"]:
            if not legajo.isdigit():
                print("El legajo ingresado no es válido, por favor vuelva a ingresar un legajo que sí lo sea")
                for i in range(len(profesores["Legajo"])):
                    print(f"- {profesores['Legajo'][i]}") 
                legajo = input("Ingrese legajo del profesor a modificar: ")
                
            elif legajo not in profesores["Legajo"]:
                print("El legajo ingresado no se encuentra en la lista de profesores")
                print("Por favor, vuelva a ingresar un legajo que sí esté en la lista")
                print("\nLos legajos disponibles son: ")
                for i in range(len(profesores["Legajo"])):
                    print(f"- {profesores['Legajo'][i]}")    
                legajo = input("Ingrese legajo del profesor a modificar: ")

        legajo = int(legajo)


        if legajo in profesores["Legajo"]:
            i = profesores["Legajo"].index(legajo)
            modificar = True

            while modificar:
                print("\nQué dato del profesor desea modificar?")
                print("---------------------------")
                print("Opción 1: Legajo")
                print("Opción 2: Nombre")
                print("Opción 3: Apellido")
                print("Opción 4: DNI")
                print("Opción 5: Mail")
                print("Opción 6: Salir")
                print("---------------------------")
                opcion = input("Que opción desea elegir? ")
                # Pido la opción a modificar

                # Validación de la opción
                validarOpcion = opcion.isdigit()
                while not validarOpcion or int(opcion) not in range(1, 7):
                    print("El dato ingresado no es válido, por favor vuelva a ingresar un dato que sí lo sea")
                    print("---------------------------")
                    print("Opción 1: Legajo")
                    print("Opción 2: Nombre")
                    print("Opción 3: Apellido")
                    print("Opción 4: DNI")
                    print("Opción 5: Mail")
                    print("Opción 6: Salir")
                    print("---------------------------")
                    opcion = input("Que opción desea elegir?: ")
                    validarOpcion = opcion.isdigit()

                opcion = int(opcion)
                # Validación de la opción

                if opcion == 1:
                    print("El legajo actual es: ", profesores["Legajo"][i])
                    profesores["Legajo"][i] = int(input("Nuevo legajo: "))
                    print("Profesor modificado.")
                elif opcion == 2:
                    print("El nombre actual es: ", profesores["NombreProfesores"][i])
                    profesores["NombreProfesores"][i] = input("Nuevo nombre: ")
                    print("Profesor modificado.")
                elif opcion == 3:
                    print("El apellido actual es: ", profesores["ApellidoProfesores"][i])
                    profesores["ApellidoProfesores"][i] = input("Nuevo apellido: ")
                    print("Profesor modificado.")
                elif opcion == 4:
                    print("El DNI actual es: ", profesores["DNI"][i])
                    profesores["DNI"][i] = int(input("Nuevo DNI: "))
                    print("Profesor modificado.")
                elif opcion == 5:
                    print("El mail actual es: ", profesores["Mail"][i])
                    profesores["Mail"][i] = input("Nuevo mail: ")
                    print("Profesor modificado.")
                elif opcion == 6:
                    print("Ha salido del menú de modificación de profesores.")
                    modificar = False
        continuar = input("¿Desea modificar otro profesor? (si/no): ")
        if continuar.lower() == "si":
            modificar = True
        else:
            bandera = False
            

    return profesores

modificarProfesores(diccionarioProfesores)