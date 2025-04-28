#CREAR UNA FUNCION QUE RECIBA UNA MATRIZ Y UN ELEMENTO QUE DESEA ELIMINAR DE ESTA
#Para hacer esto vamos a buscarlo con el ID, o por el Legajo
#Ya que cualquiera de las tres matrices posee ID, o Legajo


import funciones.conversionmatriz,funciones.imprimir



#LO MODIFIQUE
def eliminarAlumno(alumnos,legajo):
    nuevoDiccionario = []
    alumnoEncontrado = False
    i = 0
    for alumno in alumnos:
        
        if int(alumno["Legajo"]) == legajo:  # Compara el legajo como cadena
            alumnoEncontrado = True
        else: 
            nuevoDiccionario.append(alumnos[i]) #Creo una nueva lista con los datos que no se desean borrar
        i+=1
    if alumnoEncontrado:
        #alumnos.remove(alumno)  # Elimina el diccionario de la lista
        print(f"Alumnos con legajo {legajo} eliminado.")
    else:
        print(f"No se encontro un alumno con el legajo {legajo}")
    return nuevoDiccionario



def eliminarEvaluacion(evaluaciones,idEval):
    filas = len(evaluaciones)
    evaluacionEncontrada = False
    nuevaMatriz = []
    for fil in range (filas):
        if len(evaluaciones[fil]) > 0 and evaluaciones[fil][0] == idEval:
            #matrizEv.pop(fil)
            evaluacionEncontrada = True
        else:
            nuevaMatriz.append(evaluaciones[fil])
    return evaluacionEncontrada,nuevaMatriz



def eliminarProfesor(profesores,legajoProfesor):
    profesorEncontrado = False
    i = 0

    while (i < len(profesores["Legajo"])) and (not profesorEncontrado) :
        if profesores["Legajo"][i] == legajoProfesor:
            profesores["Legajo"].pop(i)
            profesores["NombreProfesores"].pop(i)
            profesores["ApellidoProfesores"].pop(i)
            profesores["DNI"].pop(i)
            profesores["Mail"].pop(i)
            profesorEncontrado = True
        i += 1
    return profesorEncontrado,profesores


def eliminarElementoMenu(alumnos,evaluaciones,profesores):
    bandera = True
    print("---------------------------")
    print("Opción 1: Alumno")
    print("Opción 2: Evaluaciones")
    print("Opción 3: Profesores")
    print("Opción 4: SALIR")
    print("---------------------------")
    print()
    idMatriz= int(input("Ingrese que matriz desea modificar:  "))
    while bandera:
        while idMatriz not in [1,2,3,4]:
                print("Número de id no válido, volver a ingresar: ")
                idMatriz= int(input("Ingrese que matriz desea modificar [1,2,3,4]:  "))
        if idMatriz == 4:
            bandera = False
        else: 
            #Que alumno se desea eliminar?
            if idMatriz == 1:
                print("\nLos legajos disponibles son: ")
                for alumno in alumnos:
                    print(f"- {alumno["Legajo"]}")
                legajo = input("Ingrese el legajo del alumno que desea eliminar: ")
                if legajo.isdigit():
                    legajo = int(legajo)
                else:
                    print("El legajo ingresado no es válido, por favor vuelva a ingresar un legajo que sí lo sea")
                    print("\nLos Legajos de Alumnos disponibles son: ")
                    for alumno in alumnos:
                        print(f"- {alumno["Legajo"]}")
                        legajo = int(input("Ingrese el legajo a modificar: "))
                if type(alumnos[0]) == list:
                    alumnos = funciones.conversionmatriz.conversionMatrizADiccioario(alumnos)
                    alumnos = eliminarAlumno(alumnos,legajo)
                    funciones.imprimir.imprimirMatrizDiccAlumnos(alumnos)
                else:
                    alumnos = eliminarAlumno(alumnos,legajo)
                    funciones.imprimir.imprimirMatrizDiccAlumnos(alumnos)
                    
                
                
            #Que evaluación desea eliminar?
            elif idMatriz == 2:
                print("\nIDs de las evaluaciones disponibles: ")
                for evaluacion in evaluaciones:
                    print(f"- {evaluacion[0]}")
                    #Muestra el id de cada evaluación
                idEval = input("Ingrese el ID de la evaluación que se desea eliminar: ")
                while not idEval.isdigit():
                    print("El ID ingresado no es válido, por favor vuelva a ingresar un ID que sí lo sea")
                    print("\nIDs de las evaluaciones disponibles: ")
                    for evaluacion in evaluaciones:
                        print(f"- {evaluacion[0]}")
                        #Muestra el id de cada evaluación
                    idEval = input("Ingrese el ID de la evaluación a modificar: ")

                idEval = int(idEval)
                evaluacionEncontrada,evaluaciones = eliminarEvaluacion(evaluaciones,idEval)
                funciones.imprimir.imprimirMatrizEv(evaluaciones)
                if evaluacionEncontrada:
                    print(f"Evaluación con id {idEval} eliminada.")
                elif not evaluacionEncontrada:
                    print(f"La evaluación {idEval} no ha sido encontrada!")


            #Que profesor se desea eliminar?
            else:
                for i in range(len(profesores["Legajo"])):
                    print(f"- {profesores['Legajo'][i]}") 
        
                legajoP = input("Ingrese legajo del profesor a modificar: ")
                # Validación de legajo
                while not legajoP.isdigit() or int(legajoP) not in profesores["Legajo"]:
                    if not legajoP.isdigit():
                        print("El legajo ingresado no es válido, por favor vuelva a ingresar un legajo que sí lo sea")
                        for i in range(len(profesores["Legajo"])):
                            print(f"- {profesores['Legajo'][i]}") 
                        legajoP = input("Ingrese legajo del profesor a modificar: ")
                        
                    elif legajoP not in profesores["Legajo"]:
                        print("El legajo ingresado no se encuentra en la lista de profesores")
                        print("Por favor, vuelva a ingresar un legajo que sí esté en la lista")
                        print("\nLos legajos disponibles son: ")
                        for i in range(len(profesores["Legajo"])):
                            print(f"- {profesores['Legajo'][i]}")    
                        legajoP = input("Ingrese legajo del profesor a modificar: ")

                legajoP = int(legajoP)
                
                profesorEncontrado,profesores = eliminarProfesor(profesores,legajoP)
                funciones.imprimir.imprimirDiccionarios(profesores)
                if profesorEncontrado:
                    print(f"Profesor con legajo {legajoP} eliminado. ")
                elif not profesorEncontrado:
                    print(f"No se encontró el profesor con el legajo {legajoP}")
            print()
            print("---------------------------")
            print("Opción 1: Alumno")
            print("Opción 2: Evaluaciones")
            print("Opción 3: Profesores")
            print("Opción 4: SALIR")
            print("---------------------------")
            print()
            idMatriz= int(input("Ingrese que matriz desea modificar:  "))
    return alumnos,evaluaciones,profesores


