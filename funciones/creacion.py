import re

#CREACIÓN DE LA MATRIZ ALUMNOS
def crearMatrizAlumnos():
    # Inicializar la matriz
    matriz_datos = []

    continuar = "si"
    contador = 1

    while continuar == "si":
        print("\nPersona", contador)
        
        legajo = input("Ingrese el legajo del alumno: ")
        legajoEnmascarado = re.sub("[0-2]{3}[0-9]{4}",'120XXXX',legajo)
        print(legajoEnmascarado)
        nombre = input("Nombre Alumno: ")
        apellidoAlumno = input("Apellido : ")
        #PODEMOS VALIDAR EL DNI
        dni = int(input("DNI: "))
        mail = input("Ingrese el email del alumno: ")
        patron = r'\@'
        coincidencias = re.findall(patron,mail)
        while len(coincidencias) == 0:
            print("Mail no válido, no ingreso el caracter '@' ")
            mail = input("Ingrese el email del alumno: ")
            patron = r'\@'
            coincidencias = re.findall(patron,mail)



        matriz_datos.append([legajo, nombre, apellidoAlumno , dni, mail])
        contador += 1

        continuar = input("¿Deseas ingresar otra persona? (si/no): ")

    # Imprimir la matriz como tabla con tabulaciones
    print("\nMatriz de datos (Legajo | Nombre | Apellido | DNI | Mail):\n")
    
    print("Legajo".ljust(15),"Nombre".ljust(15),"Apellido".ljust(15),"DNI".ljust(15),"Mail")
    print("-" * 80)

    for fila in matriz_datos:
        print(str(fila[0]).ljust(15),fila[1].ljust(15),fila[2].ljust(15),str(fila[3]).ljust(15), fila[4])
    
    return matriz_datos

#crear_matrizAlumnos()

#CREACIÓN DE LA MATRIZ EVALUACIÓN
def crearMatrizEvaluaciones():
    # Inicializar la matriz
    matriz_datos = []

    continuar = "si"
    contador = 1

    while continuar == "si":
        print("\nEvaluación", contador)
        #
        IDEvaluacion = int(input("Ingrese el ID de la evaluación: "))
        fecha = input("Fecha de la evaluación: ")
        #dia,mes,anio = fecha[:2],fecha[3:5],fecha[6:]
        #print(dia,mes,anio)
        #dia = int(input("Ingrese dia: " ))
        #mes = int(input("Ingrese mes: "))
        #anio = int(input("Ingrese el año: "))
        #fecha = (dia, "-", mes, "-" ,anio)
        instanciaEv = input("Ingrese la instancia evaluativa: ")
        #
        materia = input("Ingrese la materia: ")
        #VALIDACION DE CALIFICACIÓN MEDIANTE FUNCIÓN LAMBDA
        validacionlambda = lambda c: c < 1 or c > 10
        calificacion = int(input("Ingrese la calificación del alumno: "))
        while validacionlambda(calificacion):
            print("Calificación no válida")
            calificacion = int(input("Ingrese nuevamente la calificación del alumno: "))

        matriz_datos.append([IDEvaluacion,fecha,instanciaEv,materia,calificacion])
        contador += 1

        continuar = input("¿Deseas ingresar otra persona? (si/no): ")

    # Imprimir la matriz como tabla con tabulaciones
    print("\nMatriz de datos (ID | Fecha | Instancia | Materia | Calificación):\n")
    
    print("ID".ljust(20),"Fecha".ljust(20),"Instancia".ljust(20),"Materia".ljust(45),"Califiación")
    print("-" * 150)

    for fila in matriz_datos:
        print(str(fila[0]).ljust(20),fila[1].ljust(20),fila[2].ljust(20),str(fila[3]).ljust(45), fila[4])
    
    return matriz_datos



#CREACIÓN DE DICCIONARIO DE PROFESORES
def crearDiccionarioProfesores():
    # Inicializar listas vacias
    Legajo = []
    NombreProfesor = []
    ApellidoProfesor = []
    DNI = []
    Mail = []

    #Encabezados del diccionario
    encabezados = ['Legajo','Nombre del Profesor','Apellido del Profesor','DNI','Mail']


    continuar = "si"
    contador = 1

    while continuar == "si":
        print("\nPersona", contador)
        #PODEMOS VALIDAR EL LEGAJO
        legajo = int(input("Ingrese el legajo del profesor: "))
        nombreProfesor = input("Nombre del profesor: ")
        apellidoProfesor = input("Apellido del profesor : ")
        #PODEMOS VALIDAR EL DNI
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

        

        #FALTA IMPRIMIR DE ALGUNA MANERA LINDA EL DICCIONARIO


        
        contador += 1

        continuar = input("¿Deseas ingresar otra persona? (si/no): ")

    #

#crearDiccionarioProfesores()