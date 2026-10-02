from paciente import Paciente

pacientes: list[Paciente] = [
    Paciente("12343212-5","ejemplo1",10,"Fonasa"),
    Paciente("12111111-4","ejemplo2",20,"Isapre")
]
def menu() -> int:
    print(''
    "Menu:\n"
    "1. Agregar Paciente\n"
    "2. Editar Paciente\n"
    "3. Eliminar Paciente\n"
    "4. Imprimir Paciente\n"
    "5. Imprimir Todos los Pacientes\n"
    "0. Salir\n")
    opcion = leer_numero("Seleccione una opcion: ")
    return opcion

def leer_numero(mensaje : str) -> int:
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Ingrese un numero adecuado")

def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente: paciente_rut = input("Esta seguro que quiere eliminar?\n"
    "ingrese el RUT del paciente:")
    if paciente.rut == paciente_rut:
        pacientes.remove(paciente)
        print("Paciente Eliminado")
    else:
        print("Paciente no encontrado")

def main()->None:
    while True:
        opcion = menu()
        if opcion == 1:
            agregar_paciente()
        elif opcion == 2:
            print("Editar Paciente")
            editar_paciente()
        elif opcion == 3:
            print("Eliminar Paciente")
            eliminar_paciente()
        elif opcion == 4:
            print("Imprimir Paciente")
            imprimir_paciente()
        elif opcion == 5:
            print("Imprimir Todos los Pacientes")
            imprimir_pacientes()
        elif opcion == 0:
            break
        else:
            print("Esa opcion no es correcta")

def editar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print("Menu\n" \
        "1. Editar Nombre\n" \
        "2. Editar Edad\n" \
        "3. Editar Prevision\n" \
        "0. Salir\n")
    opcion = leer_numero("Seleccione una opcion: ")
    if opcion == 1:
        nombre = (f"nombre actual: {paciente.nombre}\n")
        nombre = input("Ingrese el nuevo nombre: ")

        paciente.nombre = nombre
    elif opcion == 2:
        edad = (f"edad actual: {paciente.edad}\n")
        input("Ingrese la nueva edad: ")
        paciente.edad = edad
    elif opcion == 3:
        prevision = (f"prevision actual: {paciente.prevision}\n")
        print("Previsiones Disponibles\n"
        "1. Fonasa\n"
        "2. Isapre\n"
        "3. Particular\n"
        "4. Otro\n"
        "0. Salir\n")
        prevision = leer_numero("Ingrese su tipo de seguro: ")
        if prevision == 1:
            prevision = "Fonasa"
        elif prevision == 2:
            prevision = "Isapre"
        elif prevision == 3:
            prevision = "Particular"
        elif prevision == 4:
            prevision = "Otro"
        else:
            prevision = ""
            print("Opcion no Valida")
            return
        paciente.prevision = prevision

def agregar_paciente():
    rut = input("Ingrese su Rut: ")
    nombre = input("Ingrese su Nombre: ")

    edad = leer_numero("Ingrese la edad del paciente: ")
    print("Previsiones Disponibles\n"
    "1. Fonasa\n"
    "2. Isapre\n"
    "3. Particular\n"
    "4. Otro\n"
    "0. Salir\n")
    prevision = leer_numero("Ingrese su tipo de seguro: ")
    if prevision == 1:
        prevision = "Fonasa"
    elif prevision == 2:
        prevision = "Isapre"
    elif prevision == 3:
        prevision = "Particular"
    elif prevision == 4:
        prevision = "Otro"
    else:
        prevision = ""
        print("Opcion no Valida")
        return

    try: 
        nuevo_paciente = Paciente(rut, nombre, edad, prevision)
    except ValueError as e:
        print(f"Error al crear el paciente: {e}")
        return
    
    pacientes.append(nuevo_paciente)
    print("Paciente Agregado Exitosamente")
    print("-"*10)

def imprimir_pacientes()-> None:
    if pacientes:
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados")

def buscar_paciente()->Paciente | None:
    rut = input("Ingrese el Rut del paciente: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
    return None
def imprimir_paciente()-> None:
    paciente = buscar_paciente()
    if paciente: 
        print(paciente)
    else:
        print("Paciente no encontrado. ")
if __name__ == "__main__":
    main()