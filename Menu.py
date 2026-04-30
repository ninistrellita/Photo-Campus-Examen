from registrar_servicios import registrar_servicio
from editar_servicios import editar_servicio
from servicios import eliminar_servicio
while True :
    print("----------MENU---------")
    print("1. Registrar servicios")
    print("2. Editar servicios")
    print("3. Eliminar servicios")
    print("4. Salir")
    print("-----------------------")
    opcion = input("Digite opcion: ")
    print("-----------------------")

    if opcion == "1" :
        registrar_servicio()
    elif opcion == "2":
        editar_servicio()
    elif opcion == "3" :
        eliminar_servicio()
    elif opcion == "4" :
        print("Saliendo del sistema")
        break
    else:
        print("Opcion no valida")


