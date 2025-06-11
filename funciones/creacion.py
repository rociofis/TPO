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


def cargarArchivoJSON(entidad, archivo):
    try:
        with open(archivo, 'w', encoding="UTF-8") as archivo:
            json.dump(entidad, archivo, ensure_ascii=False, indent=4)
    except:
        print("No se pudo abrir el archivo")

profesores = [
    {"Legajo": 1001, "Nombre": "Juan", "Apellido": "Perez", "DNI": 32123456, "Mail": "juan.perez@gmail.com"},
    {"Legajo": 1002, "Nombre": "Tomas", "Apellido": "Penny", "DNI": 2342332, "Mail": "tomm.penny@gmail.com"},
    {"Legajo": 1003, "Nombre": "Matias", "Apellido": "Lugo", "DNI": 7438384, "Mail": "tomasLUGO@gmail.com"},
    {"Legajo": 1004, "Nombre": "Julian", "Apellido": "Fernan", "DNI": 929323, "Mail": "juafernan@gmail.com"}
]

alumnos = [
    {"Legajo":1201, "Nombre": "Juan", "Apellido": "Martinez", "DNI": 32123789, "Mail": "juan.perez14@gmail.com"},
    {"Legajo":1202, "Nombre": "María", "Apellido": "Gómez", "DNI": 33456789, "Mail": "maria.gomez@yahoo.com"},
    {"Legajo":1203, "Nombre": "Lucas", "Apellido": "Fernández", "DNI": 31222333, "Mail": "lucas.fernandez@hotmail.com"},
    {"Legajo":1204, "Nombre": "Ana", "Apellido": "López", "DNI": 34566777, "Mail": "ana.lopez@gmail.com"}
]

cargarArchivoJSON(profesores, "profesores.json")
cargarArchivoJSON(alumnos, "alumnos.json")