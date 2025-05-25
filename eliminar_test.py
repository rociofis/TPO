import funciones.eliminar


#Nosotros sabemos que la función debe devolver una lsita de diccionarios, es decir
#Que cada alumno sea un diccionario
def test_eliminarAlumno():
    alumnos = [
        {"Legajo": 120333, "Nombre":"Juan", "Apellido":"Pérez", "DNI":32123456, "Mail":"juan.perez@gmail.com"},
        {"Legajo": 120444, "Nombre":"Tomas", "Apellido":"Penny", "DNI":2342332, "Mail":"tomm.penny@gmail.com"},
    ]
    legajoEliminar = 120444
    resultado = funciones.eliminar.eliminarAlumno(alumnos,legajoEliminar)
    assert type(resultado) == list #Verifica que el resultado sea una lista, una matriz
    for alumno in resultado:
        assert type(alumno) == dict #Verifica que cada alumno sea un diccionario
        

#Nosotros sabemos que la función debe devolver una matriz, que contiene las evaluaciones
def test_eliminarEvaluacion():
    evaluaciones = [[1, "15","03","2025", "1200001", "1204565", "Parcial", "Matemática I", 8],
                    [2, "20","04","2025", "1200304", "1201243", "Final", "Programación", 9]]
    idEliminar = 2
    resultado = funciones.eliminar.eliminarEvaluacion(evaluaciones,idEliminar)
    assert type(resultado) == list #Verifica que el resultado, lo que devuelve la función sea una lista, una matriz, ya que en python las matrices son listas de listas
    for fila in resultado:
        assert type(fila) == list #Verifica que cada fila sea una lista