from Servicios import registrar_servicio

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