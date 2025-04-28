#FUNCIONES PARA IMPRIMIR LAS MATRICES Y DICCIONARIOS

def imprimirMatrizDiccAlumnos(alumnos):
    print("\n===== MATRIZ DE ALUMNOS =====")
    print("Legajo".ljust(15), "Nombre".ljust(15), "Apellido".ljust(15), "DNI".ljust(15), "Mail")
    print("-" * 80)
    for alumno in alumnos:
        #legajo_censurado = censurar_legajo(alumno[0])
        print(str(alumno["Legajo"]).ljust(15), alumno["NombreAlumno"].ljust(15), alumno["ApellidoAlumno"].ljust(15), str(alumno["DNI"]).ljust(15), alumno["Mail"].ljust(10))

def imprimirMatrizAlumnos(alumnos):
    print("\n===== MATRIZ DE ALUMNOS =====")
    print("Legajo".ljust(15), "Nombre".ljust(15), "Apellido".ljust(15), "DNI".ljust(15), "Mail")
    print("-" * 80)
    for alumno in alumnos:
        #legajo_censurado = censurar_legajo(alumno[0])
        print(str(alumno[0]).ljust(15), alumno[1].ljust(15), alumno[2].ljust(15), str(alumno[3]).ljust(15), alumno[4])

def imprimirDiccionarios(diccionario):
    #Tabla
    print("\nMatriz de datos (Legajo | Nombre | Apellido | DNI | Mail):\n")
    print(f"{'Legajo':<20}{'Nombre':<20}{'Apellido':<20}{'DNI':<20}{'Mail':<20}")
    print("-" * 100)
    for fila in zip(*diccionario.values()):
        print("".join(f"{str(item):<20}" for item in fila))

def imprimirMatrizEv(evaluaciones):
    #Tabla
    print("\nMatriz de datos (ID | Fecha | Legajo Alumno | Legajo Profesor | Instancia | Materia | Calificación):\n")
    print("ID".ljust(20), "Fecha".ljust(15),"Legajo Alumno".ljust(20),"Legajo Profesor".ljust(20), "Instancia".ljust(20), "Materia".ljust(20), "Calificación")
    print("-" * 150)
    for fila in evaluaciones:
        # Construir la fecha como cadena
        fecha_str = (f"{fila[1]}/{fila[2]}/{fila[3]}")
        # Imprimir los datos de la fila
        print(str(fila[0]).ljust(20), str(fecha_str).ljust(15),str(fila[4]).ljust(20),str(fila[5]).ljust(20), fila[6].ljust(20), str(fila[7]).ljust(20), str(fila[8]))