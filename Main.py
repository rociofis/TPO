import funciones.creacion

matriz = funciones.creacion.crear_matrizEvaluaciones()



#OPCION 1

# Función para crear la matriz de contactos
def crear_matriz():
    # Crear una matriz vacía (lista de listas)
    matriz = []
    return matriz



# Función para cargar la matriz con datos del alumno
def cargar_datos(matriz):
    # Datos de prueba (Legajo, NombreAlumno, Apellido, DNI, Email)
    datos = [
        [130890, "Juan", "Perez", "46789456", "juan.perez@gmail.com"],
        [123457, "Ana", "Garcia", "42567908", "ana.garcia@email.com"],
        [3, "Luis Martínez", "555-8765", "luis.martinez@email.com", "Calle Real 789"],
        [4, "Carla López", "555-4321", "carla.lopez@email.com", "Blvd. de la Paz 101"],
        [5, "Pedro Díaz", "555-6789", "pedro.diaz@email.com", "Calle Sol 999"]
    ]

    
    # Agregar los datos a la matriz
    for contacto in datos:
        matriz.append(contacto)

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    # Imprimir encabezados
    print(f"{'ID':<5} {'Nombre':<15} {'Teléfono':<12} {'Email':<25} {'Dirección':<20}")
    print("-" * 77)
    
    # Imprimir los datos de la matriz
    for contacto in matriz:
        print(f"{contacto[0]:<5} {contacto[1]:<15} {contacto[2]:<12} {contacto[3]:<25} {contacto[4]:<20}")

# Crear la matriz
matriz_contactos = crear_matriz()

# Cargar la matriz con los datos
cargar_datos(matriz_contactos)

# Imprimir la matriz
imprimir_matriz(matriz_contactos)


import random

#OPCION 2
def crear_matriz(filas, columnas):
    return [[0]*columnas for fil in range(filas)]

def crear_matriz2():
    matriz = [[],[],[],[],[]]
    fila = 0
    columnas = 0
    nombre = input("Ingrese el nombreAlumno ")
    while nombre != "-1":
        matriz[fila].append(nombre)
        apellido = input("Ingrese el apellido del alumno ")
        legajo = input("Ingrese el legajo del alumno ")
        DNI = input("Ingrese el DNI del alumno ")
        email = input("Ingrese el email del alumno ")
        matriz[fila][columnas].append(apellido,legajo,DNI,email)
    if nombre == "-1":
            print("Ustede ha terminado de cargar los datos de los alumnos")
    return matriz


# LA OPCION DEFINITIVA
def crear_matrizAlumnos():
    # Inicializar la matriz
    matriz_datos = []

    continuar = "si"
    contador = 1

    while continuar == "si":
        print("\nPersona", contador)
        #PODEMOS VALIDAR EL LEGAJO
        legajo = int(input("Ingrese el legajo del alumno: "))
        nombre = input("Nombre Alumno: ")
        apellidoAlumno = input("Apellido : ")
        #PODEMOS VALIDAR EL DNI
        dni = int(input("DNI: "))
        mail = input("Ingrese el email del alumno: ")


        matriz_datos.append([legajo, nombre, apellidoAlumno , dni, mail])
        contador += 1

        continuar = input("¿Deseas ingresar otra persona? (si/no): ")

    # Imprimir la matriz como tabla con tabulaciones
    print("\nMatriz de datos (Legajo | Nombre | Apellido | DNI | Mail):\n")
    print("Legajo\t\tNombre\tApellido\tDNI\tMail")
    print("----------------------------------------")

    for fila in matriz_datos:
        print(str(fila[0]) + "\t\t" + fila[1] + "\t" + fila[2] + "\t" + str(fila[3]) + "\t" + fila[4])


# Parámetros y matrices
filas, columnas= 1, 5
matriz1, matriz2 = crear_matriz(filas, columnas), crear_matriz(filas, columnas)
print(matriz1)
print(crear_matriz2())

#crear_matrizAlumnos()


#IMPLEMENTAR DICCIONARIOS EN LA MATRIZ DE PROFESORES, PORQUE ES UNA ENTIDAD ÁTOMICA
#LA MATRIZ SE SOSTIENE PARA CUESTIONES DE INFORMACION A TRAVES DEL TIEMPO, POR EJ EVALUACIONES
