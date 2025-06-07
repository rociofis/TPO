import json




def eliminar_dato_de_profesor(archivo,profesores):
    try:
        with open(archivo, "r", encoding="UTF-8") as datos:
            profesores = json.load(datos)

        print("\nLos legajos disponibles son:")
        for profesor in profesores:
            print(f"- {profesor['Legajo']}")

        legajo = int(input("Ingrese el legajo del profesor para eliminar un dato: "))

        indice = -1
        for i in range(len(profesores)):
            if profesores[i]['Legajo'] == legajo:
                indice = i
                break

        if indice == -1:
            print("El legajo no se encuentra en la lista.")
            return

        print("\nQué dato del profesor desea eliminar?")
        print("1: Nombre")
        print("2: Apellido")
        print("3: DNI")
        print("4: Mail")
        print("5: Salir")
        opcion = int(input("Opción: "))

        campos = ["Nombre", "Apellido", "DNI", "Mail"]

        if 1 <= opcion <= 4:
            campo = campos[opcion - 1]
            profesores[indice][campo] = ""  # Vacía el campo
        elif opcion == 5:
            print("Saliendo sin cambios.")
            return
        else:
            print("Opción inválida.")
            return

        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(profesores, datos, ensure_ascii=False, indent=4)

        print("\nLista actualizada de profesores:")
        print(
            "Legajo".ljust(10),
            "Nombre".ljust(10),
            "Apellido".ljust(12),
            "DNI".ljust(10),
            "Mail"
        )
        for prof in profesores:
            print(
                str(prof['Legajo']).ljust(10),
                prof['Nombre'].ljust(10),
                prof['Apellido'].ljust(12),
                str(prof['DNI']).ljust(10),
                prof['Mail']
            )

    except Exception as e:
        print(f"Error: {e}")


def eliminarprofesor(archivo,profesores):
    try:
        with open(archivo, "r", encoding="UTF-8") as datos:
            profesores = json.load(datos)

        if not profesores:
            print("No hay profesores en la lista.")
            return

        print("\nLos legajos disponibles son:")
        for profesor in profesores:
            print(f"- {profesor['Legajo']}")

        legajo = int(input("Ingrese el legajo del profesor a eliminar: "))

        indice = -1
        for i in range(len(profesores)):
            if profesores[i]['Legajo'] == legajo:
                indice = i
                break

        if indice == -1:
            print("El legajo no se encuentra en la lista.")
            return

        confirmacion = input(f"¿Está seguro que desea eliminar al profesor con legajo {legajo}? (s/n): ").lower()
        if confirmacion != 's':
            print("Operación cancelada.")
            return

        # Eliminar al profesor completamente
        profesores.pop(indice)

        # Guardar cambios
        with open(archivo, 'w', encoding="UTF-8") as datos:
            json.dump(profesores, datos, ensure_ascii=False, indent=4)

        print("\nProfesor eliminado correctamente. Lista actualizada:")
        print(
            "Legajo".ljust(10),
            "Nombre".ljust(10),
            "Apellido".ljust(12),
            "DNI".ljust(10),
            "Mail"
        )
        for prof in profesores:
            print(
                str(prof['Legajo']).ljust(10),
                prof['Nombre'].ljust(10),
                prof['Apellido'].ljust(12),
                str(prof['DNI']).ljust(10),
                prof['Mail']
            )

    except Exception as e:
        print(f"Error: {e}")



def agregarprofesor(archivo,profesores):
    try:
        # Leer archivo
        try:
            with open(archivo, "r", encoding="UTF-8") as datos:
                profesores = json.load(datos)
        except FileNotFoundError:
            profesores = []  # Si el archivo no existe, se inicia una lista vacía

        print("\n--- Agregar un nuevo profesor ---")
        legajo = int(input("Ingrese legajo: "))

        # Verificar que el legajo no exista
        for profesor in profesores:
            if profesor['Legajo'] == legajo:
                print("Ya existe un profesor con ese legajo.")
                return

        nombre = input("Ingrese nombre: ").strip()
        apellido = input("Ingrese apellido: ").strip()
        DNI = input("Ingrese DNI: ").strip()
        mail = input("Ingrese mail: ").strip()

        nuevo_profesor = {
            "Legajo": legajo,
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": DNI,
            "Mail": mail
        }

        profesores.append(nuevo_profesor)

        with open(archivo, "w", encoding="UTF-8") as datos:
            json.dump(profesores, datos, ensure_ascii=False, indent=4)

        print("\nProfesor agregado correctamente.")

        print(
            "Legajo".ljust(10),
            "Nombre".ljust(10),
            "Apellido".ljust(12),
            "DNI".ljust(10),
            "Mail"
        )
        for prof in profesores:
            print(
                str(prof['Legajo']).ljust(10),
                prof['Nombre'].ljust(10),
                prof['Apellido'].ljust(12),
                str(prof['DNI']).ljust(10),
                prof['Mail']
            )

    except Exception as e:
        print(f"Error: {e}")



# Guardamos los profesores al archivo
mostrar_profesores()
# Modificamos un dato de profesores
modificar_Profesores('profesores.json', profesores)
# Eliminamos un dato de un profesor
eliminar_dato_de_profesor('profesores.json', profesores)
# Eliminamos todos los datos de un profesor
eliminarprofesor('profesores.json', profesores)
# Agregamos un profesor
agregarprofesor('profesores.json', profesores)