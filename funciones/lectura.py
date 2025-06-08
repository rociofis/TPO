def leerEvaluaciones(archivo):
    try:
        arch = open(archivo, 'r', encoding='UTF-8')
        linea = arch.readline()
        print(f"{"ID": <5}{"Dia": <7}{"Mes":<7}{"Año":<10}{"Legajo Alumno": <20}{"Legajo Profesor": <20}{"Instancia": <15}{"Materia": <20}{"Nota"}")
        while linea:
            id, dia, mes, año, legajo_alumno, legajo_profesor, instancia, materia, nota = linea.strip().split(',')
            print(f"{id: <5}{dia: <7}{mes:<7}{año:<10}{legajo_alumno: <20}{legajo_profesor: <20}{instancia: <15}{materia: <20}{nota}")
            linea = arch.readline().strip()
    except OSError:
        print(f"Error al leer el archivo {archivo}")
    finally:
        try:
            arch.close()
        except:
            print(f"Error al cerrar el archivo {archivo}")

leerEvaluaciones("evaluaciones.txt")

