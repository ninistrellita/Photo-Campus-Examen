import csv

def registrar_servicio ():
    nombre_servicio = input("Ingrese el servicio que desee agregar: ")
    precio_servicio = input("Ingrese el precio del servicio: ")
    evento_servico = input("Ingrese el tipo de evento: ")
    duracion_servicio = input("Ingrese la duracion del servicio: ")


    encabezado = ["Servicio" , "Precio" , "Evento" , "Duracion"]
    nuevo_servio = {"Servicios" : nombre_servicio}
    precio = {"Precio" : precio_servicio}
    evento = {"Evento" : evento_servico}
    duracion ={"Duracion" : duracion_servicio}

    servicios = [nuevo_servio,
                 precio,
                 evento,
                 duracion]

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