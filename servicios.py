def eliminar_servicio(id):
    global servicios
    servicios = [s for s in servicios if s['id'] != id]
    print(f"Servicio {id} eliminado.")
