#Función para convertir una matriz en diccionario
#En este caso vamos a convertir la matriz alumnos una vez ya creada en un diccionario


def conversionMatrizADiccioario(matriz):
    datosAlumnos = ['Legajo','NombreAlumno','ApellidoAlumno','DNI','Mail']
    #Creamos la lista de diccionarios
    alumnos = [dict(zip(datosAlumnos,fila)) for fila in matriz]
    return alumnos

def convertirDiccionarioEnMatriz(alumnos):
    matrizAlumnos = []
    for alumno in alumnos:
        fila = [
            alumno["Legajo"],
            alumno["NombreAlumno"],
            alumno["ApellidoAlumno"],
            alumno["DNI"],
            alumno["Mail"]
        ]
        matrizAlumnos.append(fila)
    return matrizAlumnos



#PRUEBA DE CODIGO
#matriz = creacion.crearMatrizAlumnos()
#alumnos=conversionMatrizADiccioario(matriz)
#for alumno in alumnos:
#    print(alumno)
