import re

#CREACIÓN DE LA MATRIZ ALUMNOS
def crearMatrizAlumnos(alumnos):
    # Inicializar la matriz

    continuar = "si"
    contador = 1

    while continuar.lower() == "si":
        print("\nPersona", contador)
        
        legajo = input("Ingrese el legajo del alumno: ")
        legajoEnmascarado = re.sub("[0-2]{3}[0-9]{4}",'120XXXX',legajo)
        print(legajoEnmascarado)
        nombre = input("Nombre Alumno: ")
        apellidoAlumno = input("Apellido : ")

        dni = int(input("DNI: "))
        mail = input("Ingrese el email del alumno: ")
        patron = r'\@'
        coincidencias = re.findall(patron,mail)
        while len(coincidencias) == 0:
            print("Mail no válido, no ingreso el caracter '@' ")
            mail = input("Ingrese el email del alumno: ")
            patron = r'\@'
            coincidencias = re.findall(patron,mail)



        alumnos.append([legajo, nombre, apellidoAlumno , dni, mail])
        contador += 1

        continuar = input("¿Deseas ingresar otra persona? (si/no): ")

    
    return alumnos



#CREACIÓN DE LA MATRIZ EVALUACIÓN
def CrearMatrizEvaluaciones(evaluaciones):
    # Inicializar la matriz
    #matrizEvaluaciones = []

    continuar = "si"
    contador = 1

    while continuar.lower() == "si":
        print("\nEvaluación", contador)
    
        IDEvaluacion = int(input("Ingrese el ID de la evaluación: "))
        dia=int(input("ingrese dia:"))
        mes=int(input("ingrese el mes:"))
        anio=int(input("ingrese el año:"))
        fecha = (dia, mes, anio)
        legajoAlumno = int(input("Ingrese el legajo del alumno: "))
        legajoProfesor = int(input("Ingrese el legajo del profesor: "))
        instanciaEv = input("Ingrese la instancia evaluativa(Parcial/Final/Recuperatorio): ")
        materia = input("Ingrese la materia: ")

        if len(materia) > 10:
            palabras = materia.split()
            if len(palabras) > 1:
                if palabras[1].lower() == "de" and len(palabras) >2:
                    materiaReducida = palabras[0][:4] + " " + palabras[2]
                else:
                    materiaReducida = palabras[0] + " " + palabras[1][:3]
            else:
                materiaReducida = materia
        else:
            materiaReducida = materia
        conjuntomaterias={materia}
        conjuntomaterias.add(materiaReducida)
    


        #VALIDACION DE CALIFICACIÓN MEDIANTE FUNCIÓN LAMBDA
        validacionlambda = lambda c: c < 1 or c > 10
        calificacion = int(input("Ingrese la calificación del alumno: ")) 
        while validacionlambda(calificacion):
            print("Calificación no válida")
            calificacion = int(input("Ingrese nuevamente la calificación del alumno: "))

        evaluaciones.append([IDEvaluacion,dia,mes,anio,legajoAlumno,legajoProfesor,instanciaEv,conjuntomaterias,calificacion])
        contador += 1

        continuar = input("¿Deseas ingresar otra evaluación? (si/no): ")

    return evaluaciones




#CREACIÓN DE DICCIONARIO DE PROFESORES
def crearDiccionarioProfesores(profesores):
    # Inicializar listas vacias
    


    continuar = "si"
    contador = 1

    while continuar.lower() == "si":
        print("\nPersona", contador)
    
        legajo = int(input("Ingrese el legajo del profesor: "))
        nombreProfesor = input("Nombre del profesor: ")
        apellidoProfesor = input("Apellido del profesor : ")
    
        dni = int(input("DNI: "))
        mail = input("Ingrese el email del profesor: ")

        # Agregar los datos al diccionario
        profesores["Legajo"].append(legajo)
        profesores["NombreProfesores"].append(nombreProfesor)
        profesores["ApellidoProfesores"].append(apellidoProfesor)
        profesores["DNI"].append(dni)
        profesores["Mail"].append(mail)

        
        contador += 1

        continuar = input("¿Deseas ingresar otra persona? (si/no): ")

    return profesores
    
