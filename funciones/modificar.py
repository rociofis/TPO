#La idea sería acceder a la columna que se desea modificar atraves de su indice y compararlo con un if anidado
#Y a su vez con algún método comparar la posición del dato a buscar, y acceder a la matriz con este indice y con la posicion del if

#matrizAlumnos = creacion.CrearMatrizAlumnos()
#alumnosDiccionario = conversionmatriz.conversionMatrizADiccioario(matrizAlumnos)
#matrizEvaluaciones = creacion.CrearMatrizEvaluaciones()
#diccionarioProfesores = creacion.crearDiccionarioProfesores()

#Se crea la matriz de alumnos y se convierte a diccionario
#Se crea la matriz de evaluaciones
#Se crea la matriz de profesores y se convierte a diccionario
import json
import re

def ingresarDNI(mensaje):
    while True:
        try:
            dni = int(input(mensaje))
            if dni < 1000000 or dni > 99999999:
                print("El DNI debe tener entre 7 y 8 dígitos.")
            else:
                return dni
        except ValueError:
            print("Se esperaba un numero entero para el DNI.")

def validarOpciones(opciones, mensaje):
    while True:
        try:
            opcion = (int(input(mensaje)))
            assert opcion in opciones
            break
        except ValueError:
            print("Se esperaba que ingrese un número")
            print("Vuelva a ingresarlo")
        except AssertionError:
            print("Opción no válida, por favor elija una de las siguientes opciones:", opciones)
    return opcion

def ingresarNumeros(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            break
        except ValueError:
            print("Se esperaba que ingrese un número")
            print("Vuelva a ingresarlo")
        # Tendriamos que darle la opción al usuario de que pueda dejar de intentar de ingresar?
    return num

def ingresarCadenas(mensaje):
    while True:
        try:
            texto = input(mensaje)
            texto = texto.strip()  # Elimina espacios al inicio y al final
            assert(texto.isalpha())
            break
        except AssertionError :
            print("Se esperaba que ingrese una cadena de texto")
            print("Vuelva a ingresarlo!")
    return texto

def validarMail2(mensaje):
    while True:
        try:
            mail = input(mensaje)
            assert(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", mail))
            break
        except AssertionError:
            print("Formato de mail no válido: '..'@''..'.com ")
    return mail


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



def modificarEvaluacionArchivoSimple(nombre_archivo):
    #idModificar = input("Ingrese el ID de la evaluación a modificar: ")
    evaluaciones = []

    try: #Abre el archivo y lee las evaluaciones
        #Se abre el archivo y se leen las evaluaciones
        with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
            linea = archivo.readline()
            while linea:
                evaluaciones.append(linea.strip().split(';'))
                linea = archivo.readline()

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
            for evaluacion in evaluaciones:
                print(f"- {evaluacion[0]}")
                #Muestra el id de cada evaluación

            idModificar = input("Ingrese el ID de la evaluación a modificar: ")

            while not idModificar.isdigit():
                print("El ID ingresado no es válido, por favor vuelva a ingresar un ID que sí lo sea")
                print("\nIDs de las evaluaciones disponibles: ")
                for evaluacion in evaluaciones:
                    print(f"- {evaluacion[0]}")
                    #Muestra el id de cada evaluación
                idModificar = input("Ingrese el ID de la evaluación a modificar: ")

            idModificar = int(idModificar)

            idEncontrado = False
            for evaluacion in evaluaciones:
                if int(evaluacion[0]) == idModificar:
                    idEncontrado = True

                    if opcion == 1:
                        print(f"La fecha actual es: {evaluacion[1]}/{evaluacion[2]}/{evaluacion[3]}")
                        print("Formato de fecha: dd/mm/aaaa") #Se verifica que se cumpla con el formato de fecha indicado
                        dia = ingresarNumeros("Ingrese el nuevo día: ")
                        if dia < 10: #En caso de que el usuario ingrese 1, aparecerá como 01
                            dia = "0" + str(dia)
                        else:
                            dia = str(dia)
                        mes = ingresarNumeros("Ingrese el nuevo mes: ")
                        if mes < 10:
                            mes = "0" + str(mes)
                        else:
                            mes = str(mes)
                        anio = ingresarNumeros("Ingrese el nuevo año: ")
                        while anio < 1990 or anio > 2025:
                            print("El año ingresado no es válido, por favor vuelva a ingresar un año entre 1990 y 2025")
                            anio = ingresarNumeros("Ingrese el nuevo año: ")
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
                    
            if idEncontrado:
                with open(nombre_archivo, 'w', encoding='UTF-8') as archivo:
                    for ev in evaluaciones:
                        archivo.write(';'.join(map(str, ev)) + '\n')
                print("La evaluación se ha modificado correctamente en el archivo.")
            else:
                print("El ID ingresado no se encuentra en la lista de evaluaciones")
                print("Por favor, vuelva a ingresar un ID que sí esté en la lista")
                print("\nIDs de las evaluaciones disponibles: ")
                for evaluacion in evaluaciones:
                    print(f"- {evaluacion[0]}")
    except OSError as mensaje:
        print(f"Error al leer el archivo {nombre_archivo}: {mensaje}")
    except ValueError as mensaje:
        print(f"Error al convertir los datos: {mensaje}")

#modificarEvaluacionArchivoSimple("evaluaciones.txt")



def modificarArchivosJSON(archivo, tipoDato):
    try:
        with open(archivo, "r", encoding="UTF-8") as datos:
            entidad = json.load(datos)
        if not entidad:
                assert False
        bandera = True
        while bandera:
            legajos = [enti["Legajo"] for enti in entidad]
            print("\nLos legajos disponibles son:")
            for legajo in legajos:
                print(f"- {legajo}")

            legajoAModificar = ingresarNumeros(f"Ingrese el legajo del {tipoDato} que se desea modificar: ")
            if legajoAModificar in legajos:
                indice = legajos.index(legajoAModificar)
                print(f"{tipoDato.capitalize()} encontrado con legajo {legajoAModificar}.")
                bandera2 = True
                while bandera2:
                    print(f"\nDatos de {tipoDato}: ")
                    print(
                        "Legajo".ljust(10),
                        "Nombre".ljust(10),
                        "Apellido".ljust(12),
                        "DNI".ljust(10),
                        "Mail"
                    )
                    print(
                        str(entidad[indice]['Legajo']).ljust(10),
                        entidad[indice]['Nombre'].ljust(10),
                        entidad[indice]['Apellido'].ljust(12),
                        str(entidad[indice]['DNI']).ljust(10),
                        entidad[indice]['Mail']
                    )
                    opcionesValidas = [1, 2, 3, 4, 5]
                    opcion = validarOpciones(opcionesValidas, f"\nQué dato del {tipoDato} desea modificar?" \
                        "\n---------------------------" \
                        "\nOpción 1: Nombre" \
                        "\nOpción 2: Apellido" \
                        "\nOpción 3: DNI" \
                        "\nOpción 4: Mail" \
                        "\nOpción 5: Salir" \
                        "\n---------------------------" \
                        "\nQue opción desea elegir?: ")

                    if opcion == 1:
                        print("El nombre actual es:", entidad[indice]["Nombre"])
                        entidad[indice]["Nombre"] = ingresarCadenas("Nuevo nombre: ").capitalize()
                    elif opcion == 2:
                        print("El apellido actual es:", entidad[indice]["Apellido"])
                        entidad[indice]["Apellido"] = ingresarCadenas("Nuevo apellido: ").capitalize()
                    elif opcion == 3:
                        print("El DNI actual es:", entidad[indice]["DNI"])
                        entidad[indice]["DNI"] = ingresarDNI("Nuevo DNI: ")
                    elif opcion == 4:
                        print("El mail actual es:", entidad[indice]["Mail"])
                        entidad[indice]["Mail"] = validarMail2("Nuevo mail: ")
                    elif opcion == 5:
                        print(f"Saliendo de la modificacion de {tipoDato} con legajo {legajoAModificar}..")
                        bandera2 = False

                    if opcion in opcionesValidas[0:4]:  # Si no es la opción de salir
                        with open(archivo, 'w', encoding="UTF-8") as datos:
                            json.dump(entidad, datos, ensure_ascii=False, indent=4)
                        print("El dato se ha modificado correctamente.")
            else:
                print(f"No se encontró un {tipoDato} con legajo {legajoAModificar}.")
            continuar = ingresarCadenas(f"¿Desea modificar otro {tipoDato}? (si/no): ").lower()
            while continuar not in ["si", "no"]:
                print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")
                continuar = ingresarCadenas(f"¿Desea modificar otro {tipoDato}? (si/no): ").lower()
            if continuar == "no":
                print("Saliendo de la modificación.")
                bandera = False

            print(f"\nLista actualizada de datos de {tipoDato} :")
            print(
                "Legajo".ljust(10),
                "Nombre".ljust(10),
                "Apellido".ljust(12),
                "DNI".ljust(10),
                "Mail"
            )
            for enti in entidad:
                print(
                    str(enti['Legajo']).ljust(10),
                    enti['Nombre'].ljust(10),
                    enti['Apellido'].ljust(12),
                    str(enti['DNI']).ljust(10),
                    enti['Mail']
                )
    except AssertionError:
        print(f"El archivo está vacío, no hay {tipoDato}s para modificar")
    except Exception as e:
        print(f"Error: {e}")

#print("El legajo no se encuentra en la lista.")

modificarArchivosJSON("profesores.json", "profesor")

#modificarArchivosJSON("alumnos.json", "Ingrese el legajo del alumno a modificar: ", "¿Desea modificar otro alumno? (si/no): ", "profesor")