#CREAR UNA FUNCION QUE RECIBA UNA MATRIZ Y UN ELEMENTO QUE DESEA ELIMINAR DE ESTA
#Para hacer esto vamos a buscarlo con el ID, o por el Legajo
#Ya que cualquiera de las tres matrices posee ID, o Legajo


#import funciones.conversionmatriz,funciones.imprimir
import json

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

def eliminarAlumno(alumnos,legajo):
    alumnoEncontrado = False
    bandera = True
    i = 0
    while bandera and i < len(alumnos):
        if legajo in alumnos[i].values():
            alumnoEncontrado = True
            alumnos.pop(i)  # Elimina el diccionario de la lista
            bandera = False
        i += 1
    if alumnoEncontrado:
        print(f"Alumnos con legajo {legajo} eliminado.")
    else:
        print(f"No se encontro un alumno con el legajo {legajo}")
    return alumnos

'''
PRUEBAS:
alumnos = [{"Legajo": 120333, "Nombre":"Juan", "Apellido":"Pérez", "DNI":32123456, "Mail":"juan.perez@gmail.com"},
            {"Legajo": 120444, "Nombre":"Tomas", "Apellido":"Penny", "DNI":2342332, "Mail":"tomm.penny@gmail.com"},
            {"Legajo": 120111, "Nombre":"Matias", "Apellido":"Lugo", "DNI":7438384, "Mail":"tomasLUGO@gmail.com"},
            {"Legajo": 120990, "Nombre":"Julian", "Apellido":"Fernan", "DNI":929323, "Mail":"juafernan@gmail.com"}]

alumnos = eliminarAlumno(alumnos,120444)
print(alumnos)
'''

def eliminarEvaluacion(evaluaciones,idEval):
    evaluacionEncontrada = False

    for fil in range (len(evaluaciones)-1):
        if evaluaciones[fil][0] == idEval:
            evaluaciones.pop(fil)
            evaluacionEncontrada = True
    
    if evaluacionEncontrada:
        print(f"Evaluación con ID {idEval} eliminada.")
    else:
        print(f"No se encontro ninguna evaluación con ID {idEval}")

    return evaluaciones

def eliminarEvaluacionArchivos(archivo):
    evaluaciones = []

    try:
        #Leer el archivo linea por linea y va vargando la matriz
        with open(archivo,'r',encoding="UTF-8") as file:
            primerLinea = file.readline()
            if not primerLinea:
                raise AssertionError("El archivo está vacío, no hay evaluaciones para eliminar")
            evaluaciones.append(primerLinea.strip().split(";"))

            linea = file.readline()
            while linea:
                evaluaciones.append(linea.strip().split(";"))
                linea = file.readline()
        IDS = [int(eval[0]) for eval in evaluaciones]
        print("Los IDS de evaluaciones disponibles son: ")
        for id in IDS:
            print(f"- {id}")
        idEliminar = ingresarNumeros("Ingrese el ID que desea eliminar: ")
        if idEliminar in IDS:
            indice = IDS.index(idEliminar)
            print("ATENCIÓN!!!!!!!!!")
            print(f"Esta seguro que desea eliminar la evaluación con ID: {idEliminar}")
            ev = evaluaciones[indice]
            print(f"""
            Evaluación a eliminar:
            ------------------------
            ID: {ev[0]}
            Fecha: {ev[1]}/{ev[2]}/{ev[3]}
            Legajo Alumno: {ev[4]}
            Legajo Profesor: {ev[5]}
            Instancia: {ev[6]}
            Materia: {ev[7]}
            Calificación: {ev[8]}
            ------------------------
            """)
            decision = ingresarCadenas("Ingrese si o no: ")
            while decision.lower() not in ["si", "no"]:
                print("Error de ingreso. Se esperaba: si o no")
                decision = ingresarCadenas("Ingrese si o no: ")

            if decision.lower() == "si":
                evaluaciones.pop(indice)

                with open(archivo, 'w',encoding="UTF-8") as file:
                    #Necesitamos volver a convertir las lineas en texto y que este separado por ";"
                    for eval in evaluaciones:
                        file.write(";".join(eval) + "\n")
                print(f"Evaluacion con ID {idEliminar} eliminado.")
        else:
            print(f"Evaluación con ID {idEliminar} no encontrado.")
    except OSError as error:
        print("Error accediendo al archvio",error)


#eliminarEvaluacionArchivos("evaluaciones.txt")
'''
PRUEBAS:
evaluaciones = [[1, "15","03","2025", "1200001", "1204565", "Parcial", "Matemática I", 8],
                    [2, "20","04","2025", "1200304", "1201243", "Final", "Programación", 9],
                    [3, "10","05","2025", "1203854", "1204124", "Parcial", "Historia", 7],
                    [4, "05","06","2025", "1204895", "1204729", "Final", "Biología", 6]]
evaluaciones = eliminarEvaluacion(evaluaciones,3)
print(evaluaciones)
'''

def eliminarProfesor(profesores,legajoProfesor):
    profesorEncontrado = False
    i=0
    while (not profesorEncontrado) and (i < len(profesores)-1):
        for profesor in profesores:
            if int(profesor["Legajo"]) == legajoProfesor:
                profesores.remove(profesor)
                profesorEncontrado = True
        i+=1
    if profesorEncontrado:
        print(f"Profesor con legajo {legajoProfesor} eliminado.")
    else:
        print(f"No se encontro profesor con el legajo {legajoProfesor}")
    return profesores



def eliminarProfesorArchivosJSON(archivo): #no hace falta pasar profesores como parametro
    try:
        bandera = True
        while bandera:
            with open(archivo, "r",encoding="UTF-8") as file:
                profesores = json.load(file)
            if not profesores:
                assert False
            legajos = [profesor["Legajo"] for profesor in profesores]
            print("Los legajos disponibles son:")
            for legajo in legajos:
                print(f"- {legajo}")
            legajoProfeAEliminar = ingresarNumeros("Ingrese el legajo del profesor que se desea eliminar: ")
            if legajoProfeAEliminar in legajos:
                indice = legajos.index(legajoProfeAEliminar)
                print("ATENCIÓN !!!")
                print(f"Esta seguro que desea eliminar el profesor con legajo {legajoProfeAEliminar} ?")
                profesor = profesores[indice]
                print("Profesor a eliminar:")
                print("-"*15)
                print(f"Legajo: {profesor['Legajo']}")
                print(f"Nombre: {profesor['Nombre']}")
                print(f"Apellido: {profesor['Apellido']}")
                print(f"DNI: {profesor['DNI']}")
                print(f"Mail: {profesor['Mail']}")
                print("-"*15)
                decision = ingresarCadenas("Ingrese si o no: ")
                while decision.lower() not in ["si", "no"]:
                    print("Error de ingreso. Se esperaba: si o no")
                    decision = ingresarCadenas("Ingrese si o no: ")

                if decision.lower() == "si":
                    profesores.pop(indice)

                    with open(archivo,"w",encoding="UTF-8") as file:
                        json.dump(profesores,file,ensure_ascii=False, indent=4)
                    print(f"Profesor con legajo {legajoProfeAEliminar} eliminado.")
                else:
                    print("Operación cancelada por el usuario.")
            else:
                print(f"No se encontró un profesor con legajo {legajoProfeAEliminar}.")
            continuar = ingresarCadenas("Desea eliminar otro profesor? (si/no): ")
            while continuar.lower() not in ["si","no"]:
                print("Error de ingreso se esperaba: si o no")
                continuar = ingresarCadenas("Desea eliminar otro profesor? (si/no): ")
            if continuar.lower() == "no":
                bandera = False
                print("Saliendo de la función de eliminar profesor...")
    except AssertionError:
        print("El archivo está vacío, no hay profesores para eliminar")
    except(OSError) as error:
        print(f"Error accediendo al archivo, {error}.")

def eliminarArchivosJSON(archivo,tipoDato): #no hace falta pasar profesores como parametro
    try:
        bandera = True
        while bandera:
            with open(archivo, "r",encoding="UTF-8") as file:
                entidad = json.load(file)
            if not entidad:
                assert False
            legajos = [enti["Legajo"] for enti in entidad]
            print("Los legajos disponibles son:")
            for legajo in legajos:
                print(f"- {legajo}")
            legajoAEliminar = ingresarNumeros(f"Ingrese el legajo del {tipoDato} que se desea eliminar: ")
            if legajoAEliminar in legajos:
                indice = legajos.index(legajoAEliminar)
                print("ATENCIÓN !!!")
                print(f"Esta seguro que desea eliminar el {tipoDato} con legajo {legajoAEliminar} ?")
                enti = entidad[indice]
                print(f"{tipoDato.capitalize()} a eliminar:")
                print("-"*15)
                print(f"Legajo: {enti['Legajo']}")
                print(f"Nombre: {enti['Nombre']}")
                print(f"Apellido: {enti['Apellido']}")
                print(f"DNI: {enti['DNI']}")
                print(f"Mail: {enti['Mail']}")
                print("-"*15)
                decision = ingresarCadenas("Ingrese si o no: ")
                while decision.lower() not in ["si", "no"]:
                    print("Error de ingreso. Se esperaba: si o no")
                    decision = ingresarCadenas("Ingrese si o no: ")

                if decision.lower() == "si":
                    entidad.pop(indice)

                    with open(archivo,"w",encoding="UTF-8") as file:
                        json.dump(entidad,file,ensure_ascii=False, indent=4)
                    print(f"{tipoDato} con legajo {legajoAEliminar} eliminado.")
                else:
                    print("Operación cancelada por el usuario.")
            else:
                print(f"No se encontró un {tipoDato} con legajo {legajoAEliminar}.")
            continuar = ingresarCadenas(f"Desea eliminar otro {tipoDato}? (si/no): ")
            while continuar.lower() not in ["si","no"]:
                print("Error de ingreso se esperaba: si o no")
                continuar = ingresarCadenas("Desea eliminar otro {tipoDato}? (si/no): ")
            if continuar.lower() == "no":
                bandera = False
                print(f"Saliendo de la función de eliminar {tipoDato}...")
    except AssertionError:
        print(f"El archivo está vacío, no hay {tipoDato}s para eliminar")
    except(OSError) as error:
        print(f"Error accediendo al archivo, {error}.")

eliminarArchivosJSON("alumnos.json","alumno")



'''

def leerMatriaRecursividad(materia):
    if len(materia)==0:
        return 0
    else:
        letra= materia[0].lower()
        if letra in range(1,10):

COSAS PARA HACER:
Peguntarle al profe si en la funcion eliminar esta bien abrir el archivo cada vez que la persona quiere modificar al profesor, alumno, es decir, a la entidad
Que la salida por pantalla o sea siempre tabla o siempre el mismo formato
Llamar todo en el main
Hacer una prueba unitaria nueva o readaptar la de eliminar
Volver a usar tuplas 
'''
'''
profesores = [{"Legajo": 120333, "Nombre":"Juan", "Apellido":"Pérez", "DNI":32123456, "Mail":"juan.perez@gmail.com"},
            {"Legajo": 120444, "Nombre":"Tomas", "Apellido":"Penny", "DNI":2342332, "Mail":"tomm.penny@gmail.com"},
            {"Legajo": 120111, "Nombre":"Matias", "Apellido":"Lugo", "DNI":7438384, "Mail":"tomasLUGO@gmail.com"},
            {"Legajo": 120990, "Nombre":"Julian", "Apellido":"Fernan", "DNI":929323, "Mail":"juafernan@gmail.com"}]
'''
#preofesores = eliminarProfesor(profesores,1201111)
#print(profesores)

'''
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

'''
