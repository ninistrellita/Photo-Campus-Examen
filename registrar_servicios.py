import csv

def registrar_servicio ():
    nombre_servicio = input("Ingrese el servicio que desee agregar: ")
    precio_servicio = input("Ingrese el precio del servicio: ")
    evento_servicio = input("Ingrese el tipo de evento: ")
    duracion_servicio = input("Ingrese la duracion del servicio: ")


    encabezado = ["Servicio" , "Precio" , "Evento" , "Duracion"]

    servicios = [{
    "Servicio": nombre_servicio,
    "Precio": precio_servicio,
    "Evento": evento_servicio,
    "Duracion": duracion_servicio
}]

    archivo_registro = "Servicio.csv"

    try:
        with open (archivo_registro, "r") as f:
            encabezado_existe = True 
    except FileNotFoundError :
        encabezado_existe = False

    with open (archivo_registro, "a") as f:
        escritor = csv.DictWriter(f,fieldnames=encabezado)
        if not encabezado_existe :
            escritor.writeheader()
        escritor.writerows(servicios)