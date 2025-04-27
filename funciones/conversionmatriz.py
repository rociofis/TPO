#Función para convertir una matriz en diccionario
#En este caso vamos a convertir la matriz alumnos una vez ya creada en un diccionario

import creacion

def conversionMatrizADiccioario(matriz):
    datosAlumnos = ['Legajo','NombreAlumno','ApellidoAlumno','DNI','Mail']
    #Creamos la lista de diccionarios
    alumnos = [dict(zip(datosAlumnos,fila)) for fila in matriz]
    return alumnos



#PRUEBA DE CODIGO
#matriz = creacion.crearMatrizAlumnos()
#alumnos=conversionMatrizADiccioario(matriz)
#for alumno in alumnos:
#    print(alumno)
