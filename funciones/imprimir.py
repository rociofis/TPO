#FUNCIONES PARA IMPRIMIR LAS MATRICES Y DICCIONARIOS

def imprimirMatrizDiccAlumnos(alumnos):
    print(f"\n{"===== MATRIZ DE ALUMNOS =====":^{80}}")
    # Encabezados de la tabla
    print("Legajo".ljust(15), "Nombre".ljust(15), "Apellido".ljust(15), "DNI".ljust(15), "Mail")
    print("-" * 80)
    for alumno in alumnos:
        #legajo_censurado = censurar_legajo(alumno[0])
        print(str(alumno["Legajo"]).ljust(15), alumno["NombreAlumno"].ljust(15), alumno["ApellidoAlumno"].ljust(15), str(alumno["DNI"]).ljust(15), alumno["Mail"].ljust(10))

def imprimirMatrizAlumnos(alumnos):
    print(f"\n{"===== MATRIZ DE ALUMNOS =====":^{80}}")
    # Encabezados de la tabla
    print("Legajo".ljust(15), "Nombre".ljust(15), "Apellido".ljust(15), "DNI".ljust(15), "Mail")
    print("-" * 80)
    for alumno in alumnos:
        #legajo_censurado = censurar_legajo(alumno[0])
        print(str(alumno[0]).ljust(15), alumno[1].ljust(15), alumno[2].ljust(15), str(alumno[3]).ljust(15), alumno[4])

def imprimirMatrizDiccProfesores(profesores):
    print(f"\n{"===== MATRIZ DE PROFESORES =====":^{80}}")
    # Encabezados de la tabla
    print("Legajo".ljust(15), "Nombre".ljust(15), "Apellido".ljust(15), "DNI".ljust(15), "Mail")
    print("-" * 80)
    for profesor in profesores:
        print(str(profesor["Legajo"]).ljust(15), profesor["Nombre"].ljust(15), profesor["Apellido"].ljust(15), str(profesor["DNI"]).ljust(15), profesor["Mail"].ljust(10))


def imprimirMatrizEv(evaluaciones):
    #Tabla
    print(f"\n{"===== MATRIZ DE EVALUACIONES =====":^{150}}")
    # Encabezados de la tabla
    print("ID".ljust(20), "Fecha".ljust(15),"Legajo Alumno".ljust(20),"Legajo Profesor".ljust(20), "Instancia".ljust(20), "Materia".ljust(20), "Calificación")
    print("-" * 150)
    for fila in evaluaciones:
        # Construir la fecha como cadena
        fecha_str = (f"{fila[1]}/{fila[2]}/{fila[3]}")
        # Imprimir los datos de la fila
        print(str(fila[0]).ljust(20), str(fecha_str).ljust(15),str(fila[4]).ljust(20),str(fila[5]).ljust(20), fila[6].ljust(20), str(fila[7]).ljust(20), str(fila[8]))


