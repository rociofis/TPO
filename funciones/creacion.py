def cargarEvaluaciones(evaluaciones, archivo):
    try:
        lineas = [f"{id_ev},{dia},{mes},{año},{legajo_alumno},{legajo_profesor},{instancia},{materia},{nota}\n" for id_ev,
        dia, mes, año, legajo_alumno, legajo_profesor, instancia, materia, nota in evaluaciones]
        with open(archivo, 'w', encoding='UTF-8') as arch:
            arch.writelines(lineas)
    except OSError as mensaje:
        print(f"Error al grabar el archivo {archivo}: {mensaje}")



evaluaciones = [[1, "15","03","2025", "1200001", "1204565", "Parcial", "Matemática I", 8],
                [2, "20","04","2025", "1200304", "1201243", "Final", "Programación", 9],
                [3, "10","05","2025", "1203854", "1204124", "Parcial", "Historia", 7],
                [4, "05","06","2025", "1204895", "1204729", "Final", "Biología", 6]]

cargarEvaluaciones(evaluaciones, "evaluaciones.txt")
