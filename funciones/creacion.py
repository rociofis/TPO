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

    # Imprimir la matriz como tabla con tabulaciones
    print("\nMatriz de datos (Legajo | Nombre | Apellido | DNI | Mail):\n")
    
    print("Legajo".ljust(15),"Nombre".ljust(15),"Apellido".ljust(15),"DNI".ljust(15),"Mail")
    print("-" * 80)

    for fila in alumnos:
        print(str(fila[0]).ljust(15),fila[1].ljust(15),fila[2].ljust(15),str(fila[3]).ljust(15), fila[4])
    
    return alumnos



#CREACIÓN DE LA MATRIZ EVALUACIÓN
def CrearMatrizEvaluaciones(evaluaciones):
    # Inicializar la matriz
    matrizEvaluaciones = []

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

        matrizEvaluaciones.append([IDEvaluacion,fecha,legajoAlumno,legajoProfesor,instanciaEv,conjuntomaterias,calificacion])
        contador += 1

        continuar = input("¿Deseas ingresar otra evaluación? (si/no): ")

    # Imprimir la matriz como tabla con tabulaciones
    print("\nMatriz de datos (ID | Fecha | Legajo del Alumno | Legajo del Profesor | Instancia | Materia | Calificación):\n")
    
    print("ID".ljust(20),"Fecha".ljust(20),"Legajo del Alumno".ljust(20),"Legajo del Profesor".ljust(20),"Instancia".ljust(20),"Materia","Calificación")
    print("-" * 150)

    for fila in matrizEvaluaciones:
        fecha_str = f"{fila[1][0]:02d}/{fila[1][1]:02d}/{fila[1][2]}"
        print(str(fila[0]).ljust(20),fecha_str.ljust(20),str(fila[2]).ljust(20),str(fila[3]).ljust(20), fila[4].ljust(20), fila[5], str(fila[6]).ljust(20))
    
    return matrizEvaluaciones




#CREACIÓN DE DICCIONARIO DE PROFESORES
def crearDiccionarioProfesores(profesores):
    # Inicializar listas vacias
    Legajo = [profesores[0]]
    NombreProfesor = [profesores[1]]
    ApellidoProfesor = [profesores[2]]
    DNI = [profesores[3]]
    Mail = [profesores[4]]


    continuar = "si"
    contador = 1

    while continuar.lower() == "si":
        print("\nPersona", contador)
      
        legajo = int(input("Ingrese el legajo del profesor: "))
        nombreProfesor = input("Nombre del profesor: ")
        apellidoProfesor = input("Apellido del profesor : ")
      
        dni = int(input("DNI: "))
        mail = input("Ingrese el email del profesor: ")

        Legajo.append(legajo)
        NombreProfesor.append(nombreProfesor)
        ApellidoProfesor.append(apellidoProfesor)
        DNI.append(dni)
        Mail.append(mail)

        profesores = {
            'Legajo': Legajo,
            'NombreProfesores':NombreProfesor,
            'ApellidoProfesores':ApellidoProfesor,
            'DNI':DNI,
            'Mail':Mail
        } 
        contador += 1

        continuar = input("¿Deseas ingresar otra persona? (si/no): ")
    print(f"{"Legajo":<20}{"Nombre":<20}{"Apellido":<20}{"DNI":<20}{"Mail":<20}")
          
    for fila in zip(*profesores.values()):
        print("".join(f"{str(item):<20}" for item in fila))

    return profesores
    

