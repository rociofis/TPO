import json
def cargarEvaluaciones(evaluaciones, archivo):
    try:
        lineas = [f"{id_ev};{dia};{mes};{año};{legajo_alumno};{legajo_profesor};{instancia};{materia};{nota}\n" for id_ev,
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


def cargarProfesores():
    try:
        with open('profesores.json', 'w', encoding="UTF-8") as archivo:
            json.dump(profesores, archivo, ensure_ascii=False, indent=4)
    except:
        print("No se pudo abrir el archivo")


profesores = [
    {"Legajo": 1001, "Nombre": "Juan", "Apellido": "Perez", "DNI": 32123456, "Mail": "juan.perez@gmail.com"},
    {"Legajo": 1002, "Nombre": "Tomas", "Apellido": "Penny", "DNI": 2342332, "Mail": "tomm.penny@gmail.com"},
    {"Legajo": 1003, "Nombre": "Matias", "Apellido": "Lugo", "DNI": 7438384, "Mail": "tomasLUGO@gmail.com"},
    {"Legajo": 1004, "Nombre": "Julian", "Apellido": "Fernan", "DNI": 929323, "Mail": "juafernan@gmail.com"}
]

cargarProfesores()