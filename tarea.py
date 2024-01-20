class Tarea:
    def __init__(self, nombre, descripcion, contenido, fecha_vencimiento, completada=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.contenido = contenido
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = completada

    def mostrar_tarea(self):
        estado = "Completada" if self.completada else "Pendiente"
        print(f"{self.nombre} ({estado}): {self.descripcion}, Vence el {self.fecha_vencimiento}\nContenido: {self.contenido}")
