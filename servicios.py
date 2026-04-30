import csv

def registrar_servicio ():
    nombre_servicio = input("Ingrese el servivo que desee agregar: ")
    encabezado = ["Servicios disponibles"]
    nuevo_servio = {"Servicios disponibles" : nombre_servicio}

    servicios = [nuevo_servio]

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
