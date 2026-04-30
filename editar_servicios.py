import csv
def editar_servicio():
    archivo = "Servicio.csv"
    nombre_viejo = input("Nombre del servicio a editar: ")
    nombre_nuevo = input("Nuevo nombre del servicio: ")
    encabezado = ["servicio","precio","evento","duracion"]

    filas = []
    editado = False

    
    with open(archivo, "r") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if fila["Servicio"] == nombre_viejo:
                fila["Servicio"] = nombre_nuevo
                editado = True
            filas.append(fila)

    
    if editado:
        with open(archivo, "w", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=encabezado)
            escritor.writeheader()
            escritor.writerows(filas)
        print("Servicio actualizado.")
    else:
        print("Servicio no encontrado.")
