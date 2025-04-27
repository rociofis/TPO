#CREAR UNA FUNCION QUE RECIBA UNA MATRIZ Y UN ELEMENTO QUE DESEA ELIMINAR DE ESTA
#Para hacer esto vamos a buscarlo con el ID, o por el Legajo
#Ya que cualquiera de las tres matrices posee ID, o Legajo

import creacion,conversionmatriz

def eliminarElementoMatrizAlumnos(matriz,elemento):
    filas = len(matriz) #cantidad de filas
    columnas = len(matriz[0]) #cantidad de columnas
    for fil in range(filas):
        for col in range(columnas):
            if matriz[fil][col] == elemento:
                filaParaEliminar = fil
    matriz.pop(filaParaEliminar)
    print(matriz)


def eliminarAlumno(alumnos,legajo):
    alumnoEncontrado = False
    for alumno in alumnos:
        if str(alumno["Legajo"]) == legajo:  # Compara el legajo como cadena
            alumnos.remove(alumno)  # Elimina el diccionario de la lista
            alumnoEncontrado = True
    return alumnoEncontrado

def eliminarEvaluacion(matrizEv,idEval):
    filas = len(matrizEv)
    evaluacionEncontrada = False
    for fil in range (filas):
        if len(matrizEv[fil]) > 0 and matrizEv[fil][0] == idEval:
            matrizEv.pop(fil)
            evaluacionEncontrada = True
    return evaluacionEncontrada

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
    return profesorEncontrado

def eliminarElementoMenu(alumnos,matrizEv,profesores):
    bandera = True
    print("Ingrese 1 para modificar algún dato de un alumno")
    print("Ingrese 2 para modificar algún dato de una evaluacion")
    print("Ingrese 3 para modificar algún dato de un profesor")
    print("Ingrese 4 para SALIR")
    idMatriz= int(input("Ingrese que matriz desea modificar [1,2,3,4]:  "))
    while bandera:
        while idMatriz not in [1,2,3,4]:
                print("Número de id no válido, volver a ingresar: ")
                idMatriz= int(input("Ingrese que matriz desea modificar [1,2,3,4]:  "))
        if idMatriz == 4:
            bandera = False
        else: 
            #Que alumno se desea eliminar?
            if idMatriz == 1:
                legajo = input("Ingrese el legajo del alumno que desea eliminar: ")
                alumnoEncontrado = eliminarAlumno(alumnos,legajo)
                if alumnoEncontrado:
                        print(f"Alumno con legajo {legajo} eliminado.")      
                elif not alumnoEncontrado:
                    print(f"No se encontró un alumno con el legajo {legajo}.")
                
            #Que evaluación desea eliminar?
            elif idMatriz == 2:
                idEval = int(input("Ingrese el ID de la evaluación que se desea eliminar: "))
                evaluacionEncontrada = eliminarEvaluacion(matrizEv,idEval)
                if evaluacionEncontrada:
                    print(f"Evaluación con id {idEval} eliminada.")
                elif not evaluacionEncontrada:
                    print(f"La evaluación {idEval} no ha sido encontrada!")
            #Que profesor se desea eliminar?
            else:
                legajoProfesor = int(input("Ingrese el legajo del profesor que desea eliminar: "))
                profesorEncontrado = eliminarProfesor(profesores,legajoProfesor)
                if profesorEncontrado:
                    print(f"Profesor con legajo {legajoProfesor} eliminado. ")
                elif not profesorEncontrado:
                    print(f"No se encontró el profesor con el legajo {legajoProfesor}")
            print()
            print("Ingrese 1 para modificar algún dato de un alumno")
            print("Ingrese 2 para modificar algún dato de una evaluacion")
            print("Ingrese 3 para modificar algún dato de un profesor")
            print("Ingrese 4 para SALIR")
            print()
            idMatriz= int(input("Ingrese que matriz desea modificar [1,2,3,4]:  "))




matriz = creacion.crearMatrizAlumnos()
alumnos = conversionmatriz.conversionMatrizADiccioario(matriz)
matrizEv = creacion.crearMatrizEvaluaciones()
profesores = creacion.crearDiccionarioProfesores()
eliminarElementoMenu(alumnos,matrizEv,profesores)
print(alumnos)
print(matrizEv)
print(profesores)

#El for alumno in alumnos recorre la lista alumnos, donde cada elemento es un diccionario que representa a un alumno con sus datos (por ejemplo, Legajo, NombreAlumno, etc.). El propósito del bucle es buscar un alumno cuyo Legajo coincida con el valor ingresado por el usuario y, si lo encuentra, eliminarlo de la lista.

#Detalle del funcionamiento:
#Recorrido de la lista alumnos:
#La lista alumnos contiene diccionarios, y el bucle for alumno in alumnos itera sobre cada uno de ellos.
#Comparación del Legajo:

#Dentro del bucle, se compara el valor de alumno["Legajo"] (convertido a cadena con str()) con el valor ingresado por el usuario (legajo).
#Esto asegura que la comparación sea válida, incluso si el Legajo en el diccionario es un número y el usuario ingresa una cadena.

#Eliminación del alumno:

#Si se encuentra un alumno cuyo Legajo coincide, se elimina de la lista con alumnos.remove(alumno).

#Indicador de éxito:

#La variable alumnoEncontrado se establece en True si se encuentra y elimina un alumno.
#Si no se encuentra ningún alumno con el Legajo especificado, se imprime un mensaje indicando que no se encontró.