import funciones.conversionmatriz

#Nosotros sabemos que la función conversionMatrizADiccioario recibe una matriz
#Y devuelve un diccionario para poder hacer el pasaje de tipos de datos de alumnos
#Ya que en la función crearMatrizAlumnos se agrega alumnos usando el tipo de datos matriz
#Pero para tanto modificar como eliminar datos de los alumnos, se lo trata como tipo de dato listas de diccionarios
def test_conversionMatrizADiccioario():
    alumnos = [[120333, "Juan", "Pérez", 32123456, "juan.perez@gmail.com"],
            [120444, "María", "Gómez", 33456789, "maria.gomez@yahoo.com"]]
    '''
    alumnos = [
        {"Legajo": 120333, "Nombre":"Juan", "Apellido":"Pérez", "DNI":32123456, "Mail":"juan.perez@gmail.com"},
        {"Legajo": 120444, "Nombre":"Tomas", "Apellido":"Penny", "DNI":2342332, "Mail":"tomm.penny@gmail.com"},]
    '''
    assert type(alumnos) == list
    for fila in alumnos:
        assert type(fila) == list #Verifica que cada fila sea una lista
    resultado = funciones.conversionmatriz.conversionMatrizADiccioario(alumnos)
    assert type(resultado) == list #Para ver si devuelve una lista de diccionarios
    for alumno in resultado:
        assert type(alumno) == dict #Verifica que cada alumno sea un diccionario 