import re

#FUNCIONES PARA CONTROLAR LOS ERROR POR INGRESO DE DATOS POR TECLADO


def ingresarNumeros(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            break
        except ValueError:
            print("Se esperaba que ingrese un número")
            print("Vuelva a ingresarlo")
        # Tendriamos que darle la opción al usuario de que pueda dejar de intentar de ingresar?
    return num

def validarOpciones(opciones, mensaje):
    while True:
        try:
            opcion = (int(input(mensaje)))
            assert opcion in opciones
            break
        except ValueError:
            print("Se esperaba que ingrese un número")
            print("Vuelva a ingresarlo")
        except AssertionError:
            print("Opción no válida, por favor elija una de las siguientes opciones:", opciones)
    return opcion

#La idea de la funcion ingresarNumeros es que la persona ingrese un dato por teclado
#Si este no se puede convertir en entero, en vez de que tire error y corte la ejecucion del programa
#Se controla con la excepcion de ValueError, mostrando por pantalla al usuario que se equivoco
#Y que tiene que volver a ingresar el dato, y hasta que no lo ingrese bien, va a seguir en el while True
#Hasta que una vez se ingrese un numero, va a salir del bucle con el break

def ingresarCadenas(mensaje):
    while True:
        try:
            texto = input(mensaje)
            texto = texto.strip()  # Elimina espacios al inicio y al final
            assert(texto.isalpha())
            break
        except AssertionError :
            print("Se esperaba que ingrese una cadena de texto")
            print("Vuelva a ingresarlo!")
    return texto

#La idea de esta función ingresarCadenas es que la persona ingrese por teclado un dato
#Si la persona ingresa una cadena de texto el assert toma un valor true y sale del while true con el break
#Si la persona no ingresa una cadena de texto el assert va a dar false, porque la función isaplha da false
#Por lo que lanza el error de assert y vuelve al while hasta que el usuario ingrese el dato que se le solicita correctamente


def validarMail(mail,mensaje):
    patron = r'\@'
    coincidencias = re.findall(patron,mail)
    while len(coincidencias) == 0:
        print("Mail no válido, no ingreso el caracter '@' ")
        mail = input(mensaje)
        patron = r'\@'
        coincidencias = re.findall(patron,mail)
    return mail


def validarMail2(mensaje):
    while True:
        try:
            mail = input(mensaje)
            assert(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", mail))
            break
        except AssertionError:
            print("Formato de mail no válido: '..'@''..'.com ")
    return mail

#La función validarMail2 recibe el mensaje como parametro, es decir, lo que se va a mostrar por pantalla al usuario cuando tenga que ingresar el mail
#En un bucle infinito de while true donde se sale del while si se ingresa por teclado una cadena con el formato solicitado
#Ahi sale con el break porque el assert tendra valor verdadero
#Si no se ingresa una cadena con el formato solicitado el match devolvera falso, por lo tanto el assert también
#Lo cual generara el Assertion Error y vuelve al while hasta que el usuario ingrese el mail de la manera que se lo soliciata
#

#CREACIÓN DE LA MATRIZ ALUMNOS
def crearMatrizAlumnos(alumnos):
    # Inicializar la matriz

    continuar = "si"
    contador = 1

    while continuar.lower() == "si":
        print("\nPersona", contador)

        legajo = alumnos[-1][0] + 1  # Asignar legajo automáticamente

        legajoEnmascarado = re.sub("[0-2]{3}[0-9]{4}",'120XXXX',str(legajo))
        print(legajoEnmascarado)
        nombre = ingresarCadenas("Nombre Alumno: ").strip()
        apellidoAlumno = ingresarCadenas("Apellido : ").strip()

        dni = ingresarNumeros("DNI: ")
        mailValidado = validarMail2("Ingrese el email del alumno: ").strip()

        alumnos.append([legajo, nombre, apellidoAlumno , dni, mailValidado])
        contador += 1

        continuar = ingresarCadenas("¿Deseas ingresar otra persona? (si/no): ")
        while True:
            try:
                assert(continuar.lower()=="si" or continuar.lower()=="no")
                break
            except AssertionError:
                print("Error de ingreso")
                print("Se esperaba que ingrese: si o no")
                continuar = ingresarCadenas("¿Deseas ingresar otra persona? (si/no): ")

    
    return alumnos



#CREACIÓN DE LA MATRIZ EVALUACIÓN
def CrearMatrizEvaluaciones(evaluaciones):
    # Inicializar la matriz
    #matrizEvaluaciones = []

    continuar = "si"
    contador = 1

    while continuar.lower() == "si":
        print("\nEvaluación", contador)
    
        IDEvaluacion = ingresarNumeros("Ingrese el ID de la evaluación: ")
        dia=ingresarNumeros("ingrese dia: ")
        mes=ingresarNumeros("ingrese el mes: ")
        anio=ingresarNumeros("ingrese el año:")
        fecha = (dia, mes, anio)
        legajoAlumno = ingresarNumeros("Ingrese el legajo del alumno: ")
        legajoProfesor = ingresarNumeros("Ingrese el legajo del profesor: ")
        instanciaEv = ingresarCadenas("Ingrese la instancia evaluativa(Parcial/Final/Recuperatorio): ").strip()
        materia = ingresarCadenas("Ingrese la materia: ").strip()

        if len(materia) > 10:
            palabras = materia.split()
            if len(palabras) > 1:
                if palabras[1].lower() == "de" and len(palabras) >2:
                    materiaReducida = palabras[0][:4] + " " + palabras[2]
                else:
                    materiaReducida = palabras[0] + " " + palabras[1][:3]
            else:
                materiaReducida = materia
        else:
            materiaReducida = materia
        conjuntomaterias={materia}
        conjuntomaterias.add(materiaReducida)


        #VALIDACION DE CALIFICACIÓN MEDIANTE FUNCIÓN LAMBDA
        validacionlambda = lambda c: c < 1 or c > 10
        calificacion = int(input("Ingrese la calificación del alumno: "))
        while validacionlambda(calificacion):
            print("Calificación no válida")
            calificacion = int(input("Ingrese nuevamente la calificación del alumno: "))

        evaluaciones.append([IDEvaluacion,dia,mes,anio,legajoAlumno,legajoProfesor,instanciaEv,conjuntomaterias,calificacion])
        contador += 1

        continuar = ingresarCadenas("¿Deseas ingresar otra persona? (si/no): ").strip()
        while True:
            try:
                assert(continuar.lower()=="si" or continuar.lower()=="no")
                break
            except AssertionError:
                print("Error de ingreso")
                print("Se esperaba que ingrese: si o no")
                continuar = ingresarCadenas("¿Deseas ingresar otra persona? (si/no): ")

    return evaluaciones




#MODIFIQUE ESTA FUNCION!!!!!!!!
#!!!!!

#CREACIÓN DE DICCIONARIO DE PROFESORES
def crearDiccionarioProfesores(profesores):

    continuar = "si"
    contador = 1

    while continuar.lower() == "si":
        print("\nPersona", contador)
        # profesores es una lista vacía al inicio: profesores = []
    
        #Ingresamos por teclado los datos del profesor
        legajo = ingresarNumeros("Ingrese el legajo del profesor: ")
        nombreProfesor = ingresarCadenas("Nombre del profesor: ")
        apellidoProfesor = ingresarCadenas("Apellido del profesor : ")
        dni = ingresarNumeros("DNI: ")
        mailValidado = validarMail2("Ingrese el mail del profesor: ")
        

        #Agregamos los datos del profesor para que sea un diccionario
        profesor = {
            "Legajo": legajo,
            "NombreProfesor": nombreProfesor,
            "ApellidoProfesor": apellidoProfesor,
            "DNI": dni,
            "Mail": mailValidado
        }
        profesores.append(profesor)
        
        contador += 1

        continuar = ingresarCadenas("¿Deseas ingresar otra persona? (si/no): ")
        while True:
            try:
                assert(continuar.lower()=="si" or continuar.lower()=="no")
                break
            except AssertionError:
                print("Error de ingreso")
                print("Se esperaba que ingrese: si o no")
                continuar = ingresarCadenas("¿Deseas ingresar otra persona? (si/no): ")

    return profesores
    
#profesores = []
#crearDiccionarioProfesores(profesores)
#print(profesores)
#print(type(profesores))


#COSAS POR HACER:
'''
-Cambiar profesores a diccionario de listas (LISTO)
-Controlar los errores por ingreso de datos por teclado incorrectos (LISTO)
-Validar digitos de legajo y dni
-Validar el gmail en profesores (LISTO)
-Cambiar el orden del CRUD (LISTO)
-Arreglar la función eliminar, cambiar la lógica (LISTO)
-En la funcion modificar y eliminar, cambiar como se accede a los profesores
-Mejorar lo de los conjuntos
-Mejorar lo de las tuplas
-El legajo e ID evaluación, no debería poder modificarse
-OPERADOR IN Y VALUES PARA BUSCAR LOS LEGAJOS PARA ELIMINAR
-Los legajos se tienen que agregar no de forma manual, sino que el ultimo legajo 
'''

#PREGUNTAS PARA EL PROFE:
'''
1) Preguntar si el tipo de pruba que hizo pippo esta bien agregarla



'''
