def editar_servicio():
    archivo = "Servicio.csv"
    nombre_viejo = input("Nombre del servicio a editar: ")
    nombre_nuevo = input("Nuevo nombre del servicio: ")
    
    filas = []
    editado = False

    
    with open(archivo, "r") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if fila["Servicios disponibles"] == nombre_viejo:
                fila["Servicios disponibles"] = nombre_nuevo
                editado = True
            filas.append(fila)

    
    if editado:
        with open(archivo, "w", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=["Servicios disponibles"])
            escritor.writeheader()
            escritor.writerows(filas)
        print("Servicio actualizado.")
    else:
        print("Servicio no encontrado.")
