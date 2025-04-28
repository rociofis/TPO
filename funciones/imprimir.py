#FUNCIONES PARA IMPRIMIR LAS MATRICES Y DICCIONARIOS

def imprimirMatrizDiccAlumnos(alumnos):
    print("\n===== MATRIZ DE ALUMNOS =====")
    print("Legajo".ljust(15), "Nombre".ljust(15), "Apellido".ljust(15), "DNI".ljust(15), "Mail")
    print("-" * 80)
    for alumno in alumnos:
        #legajo_censurado = censurar_legajo(alumno[0])
        print(alumno["Legajo"].ljust(15), alumno["NombreAlumno"].ljust(15), alumno["ApellidoAlumno"].ljust(15), str(alumno["DNI"]).ljust(15), alumno["Mail"])

def imprimirMatrizAlumnos(alumnos):
    print("\n===== MATRIZ DE ALUMNOS =====")
    print("Legajo".ljust(15), "Nombre".ljust(15), "Apellido".ljust(15), "DNI".ljust(15), "Mail")
    print("-" * 80)
    for alumno in alumnos:
        #legajo_censurado = censurar_legajo(alumno[0])
        print(alumno[0].ljust(15), alumno[1].ljust(15), alumno[2].ljust(15), str(alumno[3]).ljust(15), alumno[4])

def imprimirDiccionarios(diccionario):
    #Tabla
    print("\nMatriz de datos (Legajo | Nombre | Apellido | DNI | Mail):\n")
    print(f"{'Legajo':<20}{'Nombre':<20}{'Apellido':<20}{'DNI':<20}{'Mail':<20}")
    print("-" * 100)
    for fila in zip(*diccionario.values()):
        print("".join(f"{str(item):<20}" for item in fila))

def imprimirMatrizEv(evaluaciones):
    #Tabla
    print("\nMatriz de datos (ID | Fecha | Instancia | Materia | Calificación):\n")
    print("ID".ljust(20), "Fecha".ljust(20), "Instancia".ljust(20), "Materia".ljust(45), "Calificación")
    print("-" * 150)
    for fila in evaluaciones:
        fecha_str = f"{fila[1][0]:02d}/{fila[1][1]:02d}/{fila[1][2]}"
        print(str(fila[0]).ljust(20), fecha_str.ljust(20), str(fila[2]).ljust(20),str(fila[3]).ljust(20), fila[4].ljust(20), fila[5], str(fila[6]).ljust(20))