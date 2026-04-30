import csv
def eliminar_servicio():
    archivo = "Servicio.csv"
    nombre_eliminar = input("Nombre del servicio a eliminar: ")
    encabezado = ["servicio","precio","evento","duracion"]
    filas = []
   
    with open(archivo, "r") as f:
        lector = csv.DictReader(f)
        filas = [fila for fila in lector if fila["Servicio"] != nombre_eliminar]

    
    with open(archivo, "w", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=encabezado)
        escritor.writeheader()
        escritor.writerows(filas)
    print(f"Si existía el servicio '{nombre_eliminar}', ha sido eliminado.")
